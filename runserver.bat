rem --This batch file initalizes the STaTE application for hosting
@echo off

echo Spacecraft Control Center Testing and Training Environment
echo:
echo ============================================================================
echo Installing Python version 3.11.0... This might take a minute or two...
echo ============================================================================
echo Note: Please acknowledge the administrative permission window to allow Python to install
echo:

rem --Download python installer
curl "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe" -o python-installer.exe

rem --Install python
python-installer.exe /quiet InstallAllUsers=1 PrependPath=1

rem --Refresh Environmental Variables 
::echo "RefreshEnv.cmd only works from cmd.exe, please install the Chocolatey Profile to take advantage of refreshenv from PowerShell"
echo | set /p dummy="Refreshing environment variables from registry for cmd.exe. Please wait..."

goto main

:: Set one environment variable from registry key
:SetFromReg
    "%WinDir%\System32\Reg" QUERY "%~1" /v "%~2" > "%TEMP%\_envset.tmp" 2>NUL
    for /f "usebackq skip=2 tokens=2,*" %%A IN ("%TEMP%\_envset.tmp") do (
        echo/set "%~3=%%B"
    )
    goto :EOF

:: Get a list of environment variables from registry
:GetRegEnv
    "%WinDir%\System32\Reg" QUERY "%~1" > "%TEMP%\_envget.tmp"
    for /f "usebackq skip=2" %%A IN ("%TEMP%\_envget.tmp") do (
        if /I not "%%~A"=="Path" (
            call :SetFromReg "%~1" "%%~A" "%%~A"
        )
    )
    goto :EOF

:main
    echo/@echo off >"%TEMP%\_env.cmd"

    :: Slowly generating final file
    call :GetRegEnv "HKLM\System\CurrentControlSet\Control\Session Manager\Environment" >> "%TEMP%\_env.cmd"
    call :GetRegEnv "HKCU\Environment">>"%TEMP%\_env.cmd" >> "%TEMP%\_env.cmd"

    :: Special handling for PATH - mix both User and System
    call :SetFromReg "HKLM\System\CurrentControlSet\Control\Session Manager\Environment" Path Path_HKLM >> "%TEMP%\_env.cmd"
    call :SetFromReg "HKCU\Environment" Path Path_HKCU >> "%TEMP%\_env.cmd"

    :: Caution: do not insert space-chars before >> redirection sign
    echo/set "Path=%%Path_HKLM%%;%%Path_HKCU%%" >> "%TEMP%\_env.cmd"

    :: Cleanup
    del /f /q "%TEMP%\_envset.tmp" 2>nul
    del /f /q "%TEMP%\_envget.tmp" 2>nul

    :: capture user / architecture
    SET "OriginalUserName=%USERNAME%"
    SET "OriginalArchitecture=%PROCESSOR_ARCHITECTURE%"

    :: Set these variables
    call "%TEMP%\_env.cmd"

    :: Cleanup
    del /f /q "%TEMP%\_env.cmd" 2>nul

    :: reset user / architecture
    SET "USERNAME=%OriginalUserName%"
    SET "PROCESSOR_ARCHITECTURE=%OriginalArchitecture%"

    echo | set /p dummy="Finished."
    echo .


rem --Navigate to folder
cd src/SWA

rem --Use python, pip
python.exe -m pip install --upgrade --user pip --no-warn-script-location
pip install -r requirements.txt

rem --Commit migrations to SQL Database
python manage.py makemigrations
python manage.py migrate

rem --If TC account exists
:menu
echo:
cls
set /p environment="Do you already have a Test Conductor account? (y/n) "
echo:
if /i "%environment%"=="y" goto :runserver
if /i "%environment%"=="n" goto :createuser
    
:runserver 
python manage.py runserver 0.0.0.0:8000

:createuser
echo:
echo ============================================================================
echo Please setup the Test Conductor (admin) account
echo ============================================================================
echo Note: Password characters are not visible for security purposes
echo:

rem --Create admin user and runserver
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000

pause
