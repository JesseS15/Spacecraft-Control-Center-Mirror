@echo off

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
call RefreshEnv.cmd

rem --Navigate to folder
cd src/SWA

rem --Use python, pip
python.exe -m pip install --upgrade --user pip --no-warn-script-location
pip install -r requirements.txt

rem --Commit migrations to SQL Database
python manage.py makemigrations
python manage.py migrate

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