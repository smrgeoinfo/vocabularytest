#!/usr/local/bin/python
"""
github_action_main original
depends on makefile to run vocab.py
Driver file for the vocabularies GitHub Action.  Runs inside a Docker container,
with all of the vocabularies tools and dependencies copied into the Docker container.

the github workflow needs to copy output files to the docs directory
in the public github, else they disappear with the docker container when workflow
completes
original code by Dave Vieglais for iSamples project
modified by SM Richard 2023-12-14

input argumets are grabbed from environmental variables
"""

import logging
import os
import subprocess
import sys


def main():
#    logging.debug(f"environment variables are {os.environ}")
#    print(f"environment variables are {os.environ}")

    command = os.environ["INPUT_ACTION"]
    print("github_action_main: INPUT_ACTION: ", command)
    path = os.environ["INPUT_PATH"]
    path = os.path.join(path, "docs")
    input = os.environ["INPUT_INPUTTTL"]
    print(f"inputttl string: {input}")
    inputttl = input.split('|')
    # inputttl is a list of skos rdf vocabulary filenames with Turtle serialization
    # vocab_source_dir is the path to the directory that contains the source files
    for filename in inputttl:
            print(f"files to load: {filename}")

    input = os.environ["INPUT_INPUTVOCABURI"]
    print(f"inputvocaburi string: {input}")
    inputvocaburi = input.split('|')
    for auri in inputvocaburi:
            print(f"vocab URIs: {auri}")

    
    # make sure have cache directory -- this is where the sqlAlchemy db will be         
    cachepath = "cache/vocabularies.db"
    # this is the directory that holds the source SKOS ttl files.
    sourcevocabdir = "vocabulary"


    print("github_action_main: target path for output: ", path)
    if path is None:
        print("Did not receive a valid path argument so we cannot run.")
        sys.exit(-1)
    if not os.path.exists(path):
        os.makedirs(path)
        # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
        os.chmod(path, 777)
        print(f"Created {path} since it didn't exist.")

    # do function of original Makefile here
  
    for inputf in inputttl:
        result=load_cachedb(sourcevocabdir + "/" + inputf + ".ttl", cachepath)
        if (result == 0):
           print(f"load_cachedb call successful for: {inputf}")
        else:
           print(f"load_cachedb had problem processing: {inputf}")


    if command == "uijson":
        print("Generating uijson for inclusion in webUI build")
        while index < len(inputttl):
            _run_uijson_in_container(os.path.join(path, inputttl[index]+".json"), inputvocaburi[index])
            index += 1
    elif command == "docs":
        print("Generating markdown and html docs")
        index = 0
        print(f"input markdown file: {inputttl[index]}, vocab uri: {inputvocaburi[index]}")
        while index < len(inputttl):
            _run_docs_in_container(os.path.join(path, inputttl[index]+".md"), inputvocaburi[index])
            _quarto_render_html((os.path.join(path, inputttl[index]+".md")),path)
            index += 1
    else:
        print(f"Unknown command {command}.  Exiting.")
        sys.exit(-1)

def load_cachedb(inputf, cachepath):
    # tools/vocab.py --verbosity ERROR -s $(CACHE) load $(SRC)/$@

    print(f"cachdb file to load: {inputf}")
    load_args = ["--verbosity","ERROR", "-s", cachepath, "load", inputf]
    result = _run_python_in_container("/app/tools/vocab.py", load_args, f="")
    if (result == 0):
        print(f"vocab.py call successful for {inputf}")
        return 0
    else:
        print(f"vocab.py had problem processing {inputf}")
        return 1
    

def _quarto_render_html(markdown_in:str, output_path:str):
#     print("In githubActionMain: Quarto render: ",markdown_in,  output_path)
#     result = subprocess.run(["/opt/quarto/bin/quarto", "check"])
#     print("Quarto check result ", result.returncode)
     result = subprocess.run(["/opt/quarto/bin/quarto", "render", markdown_in, "-t", "html"])
     print("Quarto call result ", result.returncode)
     if (result == 0):
         print(f"Quarto call successful for {markdown_in}")
         return 0
     else:
         print(f"Quarto had problem processing {markdown_in}")
         return 1


def _run_make_in_container(target: str):
    print("In githubActionMain: make in container, target: ", target)
    subprocess.run(["/usr/bin/make", "-C", "/app", "-f", "/app/Makefile", target])


def _run_uijson_in_container(output_path: str, vocab_uri: str):
    with open(output_path, "w") as f:
        vocab_args = ["-s", "/app/cache/vocabularies.db", "uijson", vocab_uri, "-e"]
        testflag = _run_python_in_container("/app/tools/vocab.py", vocab_args, f)
        if (testflag == 0):
            print(f"Successfully wrote uijson file to {output_path}")
            return 0
        else:
            print(f"problem processing {vocab_uri}")
            return 1

def _run_docs_in_container(output_path: str, vocab_uri: str):
    with open(output_path, "w") as f:
        docs_args = ["/app/cache/vocabularies.db", vocab_uri]
        testflag = _run_python_in_container("/app/tools/vocab2mdCacheV2.py", docs_args, f)
        if (testflag == 0):
            print(f"Successfully wrote doc file to {output_path}")
            return 0
        else:
            print(f"problem processing {vocab_uri}")
            return 1

def _run_python_in_container(path_to_python_script: str, args: list[str], f):
    subprocess_args = [sys.executable, path_to_python_script]
    subprocess_args.extend(args)
    if f=="":
        result = subprocess.run(subprocess_args)
    else:
        result = subprocess.run(subprocess_args, stdout=f)
#    print("container call result ", result.returncode)
    return result.returncode




if __name__ == "__main__":
    main()
