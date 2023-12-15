# Makefile for iSamples vocabularies
#
PYTHON := python3
# The vocabulary sources, should contain the root vocabularies only, ./src/*.ttl
SRC := vocabulary
ROOT_VOCAB_SOURCES := earthenv_material_extension_mineral_group earthenv_material_extension_rock_sediment earthenv_sampled_feature_role earthenv_specimen_type
ROOT_VOCAB_URIS := ming_mineralgroupvocabulary rksd_rocksedimentvocabulary essfrole_sfrolevocabulary  esmat_essampletype
# RDFLib triplestore cache
CACHE_DIR := cache
CACHE := "$(CACHE_DIR)/vocabularies.db"
# Generated documentation
DOCS := docs

# all is the default rule if no rule is specified in the make call
.PHONY: all
#all: docs cache
# testing. calling docs is redundant with github_action_main.py
all: docs cache

# === cache ===
# Cache is a triple store containing all the vocabularies and extensions
.PHONY: cache
cache: _$(CACHE_DIR) cache_root
	@echo "in Makefile, cache rule"
_$(CACHE_DIR):
	mkdir -p $(CACHE_DIR)
# Start with the root vocabularies, otherwise extensions do nothing
# this rule generates a list of .ttl files from ROOT_VOCAB_SOURCES that trigger
#   the %.ttl rule to run vocab.py
.PHONY: cache_root
cache_root: $(patsubst %,%.ttl,$(ROOT_VOCAB_SOURCES))

# this rule applies to any target name with a .ttl extension. This will run on all
#  the $(ROOT_VOCAB_SOURCES)  because of the cache_root rule.
#  vocab.py loads the vocabs into the local squAlchemy database that is 
#  called by vocab2md.py, and used by tools/navocab
%.ttl:
	${PYTHON} tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@
	@echo "running vocab.py on "  $@


# === docs ===
# Docs are markdown generated from the vocabularies.
#   The source is the cache/vocabualries.db generated by calls to vocab.py
#   by the cache rule (above).

.PHONY: docs
docs: setup_docs $(ROOT_VOCAB_URIS)
setup_docs:
	@echo "in set_up docs makefile"
	mkdir -p $(DOCS)

# this rule applies to any target name/ will run all the $(ROOT_VOCAB_URIS)
#  becasue of the docs: rule
#  vocab2md.py generates a markdown file in the docs directory, using the vocabulary
#  baseURI (the uri for the conceptScheme in the )
%:
	@echo $(subst _,:,$@)
	@echo "running vocab2md on " $@
	${PYTHON} tools/vocab2md.py $(CACHE) $(subst _,:,$@) > $(DOCS)/$@.md

# ===HELP===
.PHONY: help
help:
	@echo "Make artifacts from vocabulary sources"
	@echo "  cache: generate triplestore cache of all vocabs and extensions"
	@echo "  clean: remove all generate artifacts"
	@echo "  docs: generate documentation in /docs"
	@echo "  uijson: generate the JSON vocabulary configurations for WebUI"



# === clean ===
# Remove any generated artifacts
clean:
	rm -rf $(DOCS)
	rm -rf $(CACHE)
