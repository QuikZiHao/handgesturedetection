@echo off
REM Change directory to the location of your project

REM Check if Python is installed
python --version
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH.
    exit /b 1
)

python -m venv handgesture
echo Virtual environment created.

call handgesture\Scripts\activate

pip installed -r requirements.txt

echo Virtual environment setup complete.
pause