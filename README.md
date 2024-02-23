# Lab 34 - Cookie Stand API

## Date - 2.23.24

## Author: Stephanie G. Johnson

## Description:

This project is a Restful API for Cookie Stands with a user facing interface. It will allow you to create, read, update, and delete cookie stands. The database will be stored in a SQLite database for local storage. However, the database is also accessible remotely from the cloud using ElephantSQL.

## Resources:

- [ElephantSQL](https://elephantsql.com/)
- [SQLite](https://www.sqlite.org/)
- [SQLite Browser](https://sqlitebrowser.org/)
- [RESTful API](https://en.wikipedia.org/wiki/Representational_state_transfer)

## Overview of Dependencies:

- Django Rest Framework
- rest_framework_simplejwt
- gunicorn
- whitenoise
- dj-database-url

For a comprehensive list of dependencies, see the [requirements.txt](requirements.txt) file.

## Install Dependencies:

```bash
pip install -r requirements.txt
```

## Usage:

```bash
python3 manage.py runserver
```

## Features:

- Create Cookie Stand
- Read Cookie Stand
- Update Cookie Stand
- Delete Cookie Stand
- User Interface
- Local Database
- Remote Database
- JWT Authentication






