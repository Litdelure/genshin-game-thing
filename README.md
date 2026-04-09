# genshin-game-thing
group project because why not

python -m venv venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.\tutorial-env\Scripts\Activate.ps1
.\venv\Scripts\Activate.ps1

py -m django --version
django-admin startproject mystie djangotutorial
py manage.py startapp polls
py manage.py runserver

Remove-Item -Recurse -Force simpleGame\.git

git add -f mysite




creating a database for each app:
python manage.py migrate
python manage.py makemigrations polls
python manage.py sqlmigrate welcome 0001