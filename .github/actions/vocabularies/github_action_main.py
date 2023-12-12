#!/usr/local/bin/python
"""
Driver file for the vocabularies GitHub Action.  Runs inside of a Docker container, with all of the vocabularies tools
and dependencies copied into the Docker container.
"""

import logging
import os
import subprocess
import sys


def main():
#    logging.debug(f"environment variables are {os.environ}")
#    print(f"environment variables are {os.environ}")

    command = os.environ["INPUT_ACTION"]
    path = os.environ["INPUT_PATH"]
    if path is None:
        print("Did not receive a valid path argument so we cannot run.")
        sys.exit(-1)
    if not os.path.exists(path):
        os.makedirs(path)
        # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
        os.chmod(path, 777)
        print(f"Created {path} since it didn't exist.")
    if command == "uijson":
        print("Generating uijson for inclusion in webUI build")
        _run_make_in_container("cache")
        _run_uijson_in_container(os.path.join(path, "material_hierarchy.json"), "mat:materialsvocabulary")
        _run_uijson_in_container(os.path.join(path, "sampledFeature_hierarchy.json"), "sf:sampledfeaturevocabulary")
        _run_uijson_in_container(os.path.join(path, "specimenType_hierarchy.json"), "spec:specimentypevocabulary")
    elif command == "docs":
        print("Generating markdown docs")
        _run_make_in_container("cache")
        _run_docs_in_container(os.path.join(path, "mat_materialsvocabulary.md"), "mat:materialsvocabulary")
        _run_docs_in_container(os.path.join(path, "sf_sampledfeaturevocabulary.md"), "sf:sampledfeaturevocabulary")
        _run_docs_in_container(os.path.join(path, "spec_specimentypevocabulary.md"), "spec:specimentypevocabulary")
    else:
        print(f"Unknown command {command}.  Exiting.")
        sys.exit(-1)


def _run_make_in_container(target: str):
    subprocess.run(["/usr/bin/make", "-C", "/app", "-f", "/app/Makefile", target])


def _run_uijson_in_container(output_path: str, vocab_type: str):
    with open(output_path, "w") as f:
        vocab_args = ["-s", "/app/cache/vocabularies.db", "uijson", vocab_type, "-e"]
        _run_python_in_container("/app/tools/vocab.py", vocab_args, f)
        print(f"Successfully wrote uijson file to {output_path}")


def _run_docs_in_container(output_path: str, vocab_type: str):
    with open(output_path, "w") as f:
        docs_args = ["/app/cache/vocabularies.db", vocab_type]
        _run_python_in_container("/app/tools/vocab2md.py", docs_args, f)
        print(f"Successfully wrote doc file to {output_path}")


def _run_python_in_container(path_to_python_script: str, args: list[str], f):
    subprocess_args = [sys.executable, path_to_python_script]
    subprocess_args.extend(args)
    subprocess.run(subprocess_args, stdout=f)


if __name__ == "__main__":
    main()
