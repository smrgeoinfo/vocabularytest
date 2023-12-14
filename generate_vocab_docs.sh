#!/bin/bash
#
# Regenerates the vocabulary markdown files from the GH sources
#
#
SCRIPT_FOLDER="$(dirname ${0})"
SOURCE_BASE="vocabulary/"
SOURCES=("earthenv_material_extension_mineral_group.ttl")
DEST_FOLDER="docs/"
mkdir -p "${DEST_FOLDER}"
for src in "${SOURCES[@]}" 
do
  fname="${src%.*}.md"
  echo "Generating ${fname}..."
  conda run -n quarto python "vocab2mdSMR.py" "${SOURCE_BASE}${src}" > "${DEST_FOLDER}${fname}"
  "quarto.exe" render "${DEST_FOLDER}${fname}" --to html
done




echo "Done.  Type 'exit' to close window. "

# "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"


