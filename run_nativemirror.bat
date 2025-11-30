@echo off
echo Checking Python...

python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python not found. Installing now...
    powershell -ExecutionPolicy Bypass -File install_python.ps1
)

echo Installing required modules...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Starting NativeMirror...
python main.py
pause