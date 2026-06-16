@echo off
title Setting up Python Virtual Environment...

:: 1. Define the virtual environment directory name
set "VENV_DIR=.venv"

:: 2. Check if the virtual environment exists, if not, create it
if not exist "%VENV_DIR%" (
    echo Creating a new virtual environment in %VENV_DIR%...
    python -m venv %VENV_DIR%
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

:: 3. Activate the virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
call "%VENV_DIR%\Scripts\activate.bat"

if exist "requirements.txt" (
    echo Installing libraries from requirements.txt...
    pip install -r requirements.txt
    echo Dependencies installed successfully.
) else (
    echo WARNING: requirements.txt file was not found in the current directory.
)

:: 4. Create shortcut to run main.py using the virtual environment
if exist "main.py" (
    echo Creating shortcut...

    powershell -NoProfile -ExecutionPolicy Bypass ^
    "$ws = New-Object -ComObject WScript.Shell; ^
    $s = $ws.CreateShortcut('%CD%\Join.lnk'); ^
    $s.TargetPath = '%CD%\%VENV_DIR%\Scripts\python.exe'; ^
    $s.Arguments = '""%CD%\main.py""'; ^
    $s.WorkingDirectory = '%CD%'; ^
    $s.IconLocation = '%CD%\%VENV_DIR%\Scripts\python.exe'; ^
    $s.Save()"

    echo Shortcut created: Run Main.lnk
) else (
    echo WARNING: main.py was not found.
)

pause