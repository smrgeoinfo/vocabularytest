#!/usr/local/bin/python
"""
This is a version of github_action_main.py set up to run offline in
an IDE environment for testing; not used by github action.
"""

import logging
import os
import subprocess
import sys
#import click
import vocab
import vocab2mdCache

# @click.option("--command", default="docs", help="docs or uijson")
# @click.option("--path", default="../vocabulary", help="path to turtle files")

def main(command, path):
#    logging.debug(f"environment variables are {os.environ}")
#    print(f"environment variables are {os.environ}")

#    command = os.environ["INPUT_ACTION"]
#    path = os.environ["INPUT_PATH"]
#     if path is None:
#         print("Did not receive a valid path argument so we cannot run.")
#         sys.exit(-1)
#     if not os.path.exists(path):
#         os.makedirs(path)
#         # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
#         os.chmod(path, 777)
#         print(f"Created {path} since it didn't exist.")

    command = 'docs'
#    command = 'uijson'
    path = 'vocabularyTemplate'

    #  essfrole_earthenv_sampled_feature_role  spec_earthenv_specimen_type
    if command == "uijson":
        print("Generating uijson for inclusion in webUI build")
#        _run_make_in_container("cache")
        _run_uijson_in_container(os.path.join(path, "earthenv_material_extension_mineral_group.json"), "ming:mineralgroupvocabulary")
        _run_uijson_in_container(os.path.join(path, "earthenv_material_extension_rock_sediment.json"), "rksd:rocksedimentvocabulary")
        _run_uijson_in_container(os.path.join(path, "earthenv_sampled_feature_role.json"), "essfrole:sfrolevocabulary")
        _run_uijson_in_container(os.path.join(path, "earthenv_specimen_type.json"), "esmat:essampletype")
# imports: http://www.w3.org/2004/02/skos/core")
    elif command == "docs":
        print("Generating markdown docs")
#        _run_make_in_container("cache")
        _run_docs_in_container(os.path.join(path, "earthenv_material_extension_mineral_group.md"), "ming:mineralgroupvocabulary")
        _run_docs_in_container(os.path.join(path, "earthenv_material_extension_rock_sediment.md"), "rksd:rocksedimentvocabulary")
        _run_docs_in_container(os.path.join(path, "earthenv_sampled_feature_role.md"), "essfrole:sfrolevocabulary")
        _run_docs_in_container(os.path.join(path, "earthenv_specimen_type.md"), "esmat:essampletype")
# imports: http://www.w3.org/2004/02/skos/core")
    else:
        print(f"Unknown command {command}.  Exiting.")
        sys.exit(-1)


#def _run_make_in_container(target: str):
#    subprocess.run(["/usr/bin/make", "-C", "/app", "-f", "/app/Makefile", target])


def _run_uijson_in_container(output_path: str, vocab_type: str):
    with open(output_path, "w") as f:
        vocab_args = ["-s", "../cache/vocabularies.db", "uijson", vocab_type, "-e"]
        _run_python_in_container("vocab.py", vocab_args, f)
        print(f"Successfully wrote uijson file to {output_path}")


def _run_docs_in_container(output_path: str, vocab_type: str):
    with open(output_path, "w") as f:
        docs_args = ["../cache/vocabularies.db", vocab_type]
        _run_python_in_container("vocab2mdCache.py", docs_args, f)
        print(f"Successfully wrote doc file to {output_path}")


def _run_python_in_container(path_to_python_script: str, args: list[str], f):
    subprocess_args = [sys.executable, path_to_python_script]
    subprocess_args.extend(args)
    subprocess.run(subprocess_args, stdout=f)


if __name__ == "__main__":
    main("docs","output")
