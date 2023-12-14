#!powershell.exe
#
$SCRIPT_FOLDER = (Get-Item $MyInvocation.MyCommand.Path).Directory.FullName
$SOURCE_BASE = "vocabulary/"
$SOURCES = @("earthenv_material_extension_mineral_group.ttl")
$DEST_FOLDER = "docs/"

# Create destination folder if it doesn't exist
New-Item -ItemType Directory -Force -Path $DEST_FOLDER | Out-Null

foreach ($src in $SOURCES) {
    Write-Host $src
    $fname = [System.IO.Path]::ChangeExtension($src, "md")
    Write-Host "Generating $fname..."
#    & python "vocab2mdSMR.py" ("{0}{1}" -f $SOURCE_BASE, $src) | Out-File -FilePath ("{0}{1}" -f $DEST_FOLDER, $fname)
    & "C:\Users\smrTu\miniconda3\Scripts\conda.exe" run -n quarto python "C:\Users\smrTu\OneDrive\Documents\GithubC\iSamples\metadata_profile_earth_science\vocab2mdSMR.py" ("{0}{1}" -f $SOURCE_BASE, $src) | Out-File -FilePath ("{0}{1}" -f $DEST_FOLDER, $fname)

}

# Assuming quarto is in the system PATH
quarto render ("{0}{1}" -f $DEST_FOLDER, $fname) --to html

Write-Host "Done. Type 'exit' to close window."
