'''Script to generate markdown from a SKOS vocabulary.

The generated markdown is intended for rendering with Quarto.
'''

import datetime
import sys
import textwrap
import click
import navocab
import rdflib

# dictionary to lookup namespace uris
NS = {
    "rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#", 
    "rdfs":"http://www.w3.org/2000/01/rdf-schema#",
    "owl":"http://www.w3.org/2002/07/owl#",
    "skos": "http://www.w3.org/2004/02/skos/core#",   
    "obo": "http://purl.obolibrary.org/obo/",
    "geosciml": "http://resource.geosciml.org/classifier/cgi/lithology"
}

# define namespace prefixs for rdflib calls to access skos vocab files
PFX = """
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""
INDENT = "  "

def skosT(term):
    return rdflib.URIRef(f"{NS['skos']}{term}")

def rdfT(term):
    return rdflib.URIRef(f"{NS['rdf']}{term}")

def rdfsT(term):
    return rdflib.URIRef(f"{NS['rdfs']}{term}")

def listVocabularies(g):
    '''List the vocabularies in the provided graph
    '''
    q = PFX + """SELECT ?s
    WHERE {
        ?s rdf:type skos:ConceptScheme.
    }"""
    qres = g.query(q)
    res = []
    for r in qres:
        res.append(r[0])
    return res

        
def getVocabRoot(g, v):
    """Get top concept of the specific vocabulary
    """    
    q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?s
    WHERE {
        ?s skos:topConceptOf ?vocabulary .
    }""")
    qres = g.query(q, initBindings={'vocabulary': v})
    res = []
    for row in qres:
        res.append(row[0])
    return res

def getNarrower(g, v, r):
    if v is None:
        q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?s
        WHERE {
            ?s skos:broader ?parent .
        }""")
        qres = g.query(q, initBindings={'parent': r})
    else:
        q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?s
        WHERE {
            ?s skos:inScheme ?vocabulary .
            ?s skos:broader ?parent .
        }""")
        qres = g.query(q, initBindings={'vocabulary': v, 'parent':r})
    res = []
    for row in qres:
        res.append(row[0])
    return res


def getObjects(g, s, p):
    q = rdflib.plugins.sparql.prepareQuery(PFX + """SELECT ?o
    WHERE {
        ?subject ?predicate ?o .
    }""")
    qres = g.query(q, initBindings={'subject':s, 'predicate':p})
#    print(f"getObjects query:\n {PFX} select ?o where {s} {p} ?o")
#    print("GetObjects q result len: ", len(qres))
    res = []
    for row in qres:
        res.append(row[0])
    return res


def _labelToLink(label):
    if isinstance(label, list):
        label = label[0]
    label = label.split("/")[-1]
    label = label.lower().strip()
    label = label.replace(",", "")
    label = label.replace(" ","-")
    return label
    


def termTree(g, v, r, depth=0):
    label = getObjects(g, r, skosT("prefLabel"))
    if len(label) < 1:
        label = getObjects(g, r, rdfsT("label"))
    if len(label) < 1:
        label = [r, ]
    llabel = _labelToLink(r)
    res = [f"{'    '*depth}- [{label[0]}](#{llabel})"]
    for term in getNarrower(g, v, r):
        res += termTree(g, v, term, depth=depth+1)
    return res


def termJsonTree(g, v, r, depth=0):
    label = getObjects(g, r, skosT("prefLabel"))[0]
    llabel = _labelToLink(r)
    obj = {
        "name": label,
        "target": llabel,
    }
    #res = [f"{'    '*depth}- [{label[0]}](#{llabel})"]
    children = []
    for term in getNarrower(g, v, r):
        children.append(termJsonTree(g, v, term, depth=depth+1))
    obj["children"] = children
    return obj


def describeTerm(g, t, depth=0, level=1):
    res = []
    labels = getObjects(g, t, skosT('prefLabel'))
    hl = f"{'#'*(depth+1)} "
    if len(labels) < 1:
        res.append(f"{hl} `{t}`")
    else:
        res.append(f"{hl} {labels[0].strip()}")
        for label in labels[1:]:
            res.append(f"* `{label}`")
        res.append("")
    _target = t.split("/")[-1]
    res.append("[]{" + f"#{_labelToLink(_target)}" + "}")
    res.append("")
    res.append(f"Concept: [`{t.split('/')[-1]}`]({t})")
    broader = getObjects(g, t, skosT('broader'))
    if len(broader) > 0:
        res.append("")
        res.append("Child of:")
        for b in broader:
            bt = b.split('/')[-1]
            res.append(f" [`{bt}`](#{bt})")
    res.append("")
    # The textual description will be present in rdfs:comment or
    # skos:definition. 
    comments = []    
    for comment in getObjects(g, t, rdfsT('comment')):
        comments.append(comment)
    for comment in getObjects(g, t, skosT('definition')):
        comments.append(comment)
    for comment in comments:
        lines = textwrap.wrap(
                    comment, 
                    width=70
                    )
        res += lines
    seealsos = getObjects(g, t, rdfsT('seeAlso'))
    if len(seealsos) > 0:
        res.append("")
        res.append("See Also:")
        res.append("")
        for seealso in seealsos:
            res.append(f"* [{seealso.n3(g.namespace_manager)}]({seealso})")    
    return res

def describeNarrowerTerms(g, v, r, depth=0, level=[]):
    res = []
    terms = getNarrower(g, v, r)
    for term in terms:
        res += describeTerm(g, term, depth=depth)
        res.append("")
        res += describeNarrowerTerms(g, v, term, depth=depth+1)
    return res

def describeVocabulary(G, V):
    res = []
    level = [1, ]
#    print("vocab, frm vocab2md/describeVocab:", V)
    title = getObjects(G, V, skosT("prefLabel"))[0]
    res.append("---")
    res.append("comment: | \n  WARNING: This file is generated. Any edits will be lost!")
    res.append(f"title: \"{title.strip()}\"")
    res.append(f"date: \"{datetime.datetime.now().replace(tzinfo=datetime.timezone.utc).isoformat()}\"")
    res.append("subtitle: |")
    for comment in getObjects(G, V, skosT("definition")) + getObjects(G, V, rdfsT("comment")):
        res.append(f"  {comment.strip()}")
    res.append("execute:")
    res.append("  echo: false")
    res.append("---")
    res.append("")
    res.append("Namespace: ")
    res.append(f"[`{V}`]({V})")
    res.append("")
    res.append("**History**")
    res.append("")
    for history in getObjects(G, V, skosT("historyNote")):
        res.append(f"* {history}")
    res.append("")
    res.append("**Concepts**")
    res.append("")
    depth = 1
    roots = getVocabRoot(G, V)
    narrower_v = None
    for root in roots:
        res += termTree(G, narrower_v, root, depth=0)
        res.append("")
    #res.append("```{ojs}")
    ##res.append("import {Tree} from '@d3/tree'")
    #res.append(TREE_CHART_SCRIPT)
    #res.append(f"vocab_terms=JSON.parse({json.dumps(json.dumps(termJsonTree(G, V, roots[0], depth=0)))});")
    #res.append(TREE_CHART_BLOCK)
    #res.append("```")
    for aroot in roots:
        res += describeTerm(G, aroot, depth=depth, level=level)
        res.append("")
        res += describeNarrowerTerms(G, narrower_v, aroot, depth=depth+1, level=level)
        res.append("")
    return res

@click.command()
@click.argument("source")
@click.argument("vocabulary")
def main(source, vocabulary):
    """Generate Pandoc markdown from a SKOS vocabulary.

    SOURCE is a navocab triplestore (sqlite database created by rdflib).

    VOCABULARY is a URI for a vocabulary root (e.g. the skos:ConceptScheme) within SOURCE

    Output to STDOUT.
    """
    source = f"sqlite:///{source}"
    store = navocab.VocabularyStore(storage_uri=source)
#    print("vocablist:",store.vocabulary_list())
#    print("graph to pass to describe vocab:", repr(store._g))
    res = []

    #TODO: This is a bit of quick hack using the internal graph of VocabularyStore.
    #      describeVocabulary should leverage functionality of navocab to
    #      access the vocabulary graphs.

    vocabulary = store.expand_name(vocabulary)
    res.append(describeVocabulary(store._g, vocabulary))
    for doc in res:
        for line in doc:
            print(line)
    return 0

if __name__ == "__main__":
    sys.exit(main())