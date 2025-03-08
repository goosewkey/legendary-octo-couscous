@echo off
color 0a
echo ================================
echo  Installing requirements...
echo ================================
color 1

:: Install dependencies from requirements.txt
pip install -r requirements.txt

:: Check if pip install was successful
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies.
    pause
    exit /b
)

:: Purge pip cache
echo Purging pip cache...
pip cache purge

echo ================================
echo  Installation Complete!
echo ================================
pause
