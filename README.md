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
Migrations are very powerful and let you change your models over time, as you develop your project, without the need to delete your database or tables and make new ones - it specializes in upgrading your database live, without losing data. We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

    Change your models (in models.py).

    Run python manage.py makemigrations to create migrations for those changes.

    Run python manage.py migrate to apply those changes to the database

python manage.py shell

>>> Question.objects.filter(id =1)

username: admin
email: lamviethai60120
pass: Hail....