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
    print("command ", command)
    path = os.environ["INPUT_PATH"]
    path = os.path.join(path, "/tools/output")
    print("input path ", path)
    if path is None:
        print("Did not receive a valid path argument so we cannot run.")
        sys.exit(-1)
    if not os.path.exists(path):
        os.makedirs(path)
        # Change to 777 so subsequent steps that deal with the directory don't run into permissions issues
        os.chmod(path, 777)
        print(f"Created {path} since it didn't exist.")

    #  essfrole_earthenv_sampled_feature_role  spec_earthenv_specimen_type
    if command == "uijson":
        print("Generating uijson for inclusion in webUI build")
        _run_make_in_container("cache")
        _run_uijson_in_container(os.path.join(path, "earthenv_material_extension_mineral_group.json"), "ming:earthenv_material_extension_mineral_group")
        _run_uijson_in_container(os.path.join(path, "earthenv_material_extension_rock_sediment.json"), "rksd:earthenv_material_extension_rock_sediment")
        _run_uijson_in_container(os.path.join(path, "earthenv_sampled_feature_role.json"), "essfrole:earthenv_sampled_feature_role")
        _run_uijson_in_container(os.path.join(path, "earthenv_specimen_type.json"), "spec:earthenv_specimen_type")
    elif command == "docs":
        print("Generating markdown docs")
        _run_make_in_container("cache")
        _run_docs_in_container(os.path.join(path, "earthenv_material_extension_mineral_group.md"), "ming:earthenv_material_extension_mineral_group")
        _run_docs_in_container(os.path.join(path, "earthenv_material_extension_rock_sediment.md"), "rksd:earthenv_material_extension_rock_sediment")
        _run_docs_in_container(os.path.join(path, "earthenv_sampled_feature_role.md"), "essfrole:earthenv_sampled_feature_role")
        _run_docs_in_container(os.path.join(path, "earthenv_specimen_type.md"), "spec:earthenv_specimen_type")
    else:
        print(f"Unknown command {command}.  Exiting.")
        sys.exit(-1)


def _run_make_in_container(target: str):
    print("In githubActionMain: make in container, target: ", target)
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
    result = subprocess.run(subprocess_args, stdout=f)
    print("container call result ", result.returncode)
    print("container call args: ", result.args)

if __name__ == "__main__":
    main()
