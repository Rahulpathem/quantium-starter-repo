# run_tests.ps1
# Runs pytest using the venv's python. Exit 0 on pass; 1 on fail.

$ErrorActionPreference = "Stop"
$python = Join-Path $PSScriptRoot 'venv\Scripts\python.exe'

if (!(Test-Path $python)) {
    Write-Host "ERROR: Could not find venv\Scripts\python.exe. Did you create the venv?"
    exit 1
}

Write-Host "Running test suite with $python ..."
& $python -m pytest -q
$code = $LASTEXITCODE

if ($code -eq 0) {
    Write-Host "All tests passed!"
    exit 0
} else {
    Write-Host "Tests failed!"
    exit 1
}
