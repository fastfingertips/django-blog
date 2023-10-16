[Requirements](requirements.txt): `pip install -r requirements.txt`

### Install Django and Create Project
- [Download Django](https://www.djangoproject.com/download/)
- setup: `pip install Django`
- version control: `django-admin --version`
- creat project: `django-admin startproject [app-name]`

### Folder Structure
- **[app-name]**
	- **manage.py**: manage.py is a command-line utility that lets you interact with this Django project in various ways.
	-	app-name/
		- **\_\_init\_\_.py**: An empty file that tells Python that this directory should be considered a Python package.
		- **settings.py**: Settings/configuration for this Django project.
		- **urls.py**: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
		- **wsgi.py**: An entry-point for WSGI-compatible web servers to serve your project.

### Run Server
```bash
cd [app-name]
python manage.py runserver
```

### Open Browser
> - django default port: `8000`
> - change port in command line: `python manage.py runserver [port]`
> - open browser and go to: `http://localhost:[port]`
> - to change the language, go to settings.py: 
> 	- `LANGUAGE_CODE = 'en-us'`
> 	- language identifiers: `http://www.i18nguy.com/unicode/language-identifiers.html`
> - to change the time zone, go to settings.py
>	- `TIME_ZONE = 'UTC'`
>	- list of time zones: `https://en.wikipedia.org/wiki/List_of_tz_database_time_zones`
> - if you want to stop server in command line: `ctrl + c`

### Migration
- Tables are created based on the models in the app
- migrate: `python manage.py migrate`

### Create App
- create app: `python manage.py startapp [app-name]`
- add app to settings.py: `INSTALLED_APPS = [app-name]`
- create model in models.py
- create migration: `python manage.py makemigrations [app-name]`
- migrate: `python manage.py migrate`

### App Structure
- **[app-name]**
	- **\_\_init\_\_.py**: An empty file that tells Python that this directory should be considered a Python package.
	- **admin.py**: You’ll register your models here so Django knows to include them in the admin interface.
	- **apps.py**: An application configuration file.
	- **migrations/**: This directory stores migration files.
	- **models.py**: This is where your models go.
	- **tests.py**: This is where your tests go.
	- **views.py**: This is where your views go.


### Create Admin
- create admin: `python manage.py createsuperuser`
- username: `admin`
- email: ``
- password: `admin`