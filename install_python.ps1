$python = Get-Command python -ErrorAction SilentlyContinue

if ($python) {
    Write-Host "Python already installed."
    exit 0
}

Write-Host "Python not found. Installing..."

$pythonInstaller = "$env:TEMP\python_installer.exe"
Invoke-WebRequest -Uri "https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe" -OutFile $pythonInstaller

Start-Process $pythonInstaller -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1 Include_test=0" -Wait

$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    Write-Host "Python installed successfully."
} else {
    Write-Host "Python installation FAILED."
}