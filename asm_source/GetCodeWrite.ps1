$sourceUrl = "https://github.com/TheGag96/CodeWrite/releases/download/v1.0.6/CodeWrite.v1.0.6.zip"
$destinationPath = Join-Path -Path $PSScriptRoot -ChildPath "CodeWrite"

# Create the destination folder if it doesn't exist
if (-not (Test-Path -Path $destinationPath -PathType Container)) {
    New-Item -Path $destinationPath -ItemType Directory | Out-Null
}

# Download the ZIP file
Write-Host "Downloading CodeWrite.v1.0.6.zip"
$zipFilePath = Join-Path -Path $destinationPath -ChildPath "CodeWrite.v1.0.6.zip"
Invoke-WebRequest -Uri $sourceUrl -OutFile $zipFilePath

# Extract the contents of the ZIP file to the destination folder
Write-Host "Extracting CodeWrite.v1.0.6.zip"
Add-Type -AssemblyName System.IO.Compression.FileSystem
[System.IO.Compression.ZipFile]::ExtractToDirectory($zipFilePath, $destinationPath)

# Remove the ZIP file after extraction
Remove-Item -Path $zipFilePath
