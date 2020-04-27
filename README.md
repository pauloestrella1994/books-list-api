# Work at Olist
## Project Description

This is a Library API that receives a CSV file, to import the authors books to database, and make a nested relationship, using Django Rest Framework.

## Installation

### Creating de virtual environment:

To install the virtual environment, set this on your folder:

```bash
$ python -m venv myvenv
```
To activate your virtual environment:

```bash
$ myvenv\Scripts\activate
```

## Install the requirements

```bash
$ pip install -r requirements-dev.txt
```

## Migrate the database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

## Start the server

```bash
$ python manage.py runserver
```

## Testing

For testing, make sure that your server is running 
correctly

And than, in order terminal, for testing the Authors list, open the folder:

```bash
$ cd Authors_list
```

And than, run the code:

```bash
$ cd pytest tests.py
```

For testing the Books list, open the folder:

```bash
$ cd core_list
```
And than, run the code:

```bash
$ cd pytest tests.py
```
Be careful that some tests can delete some data, in your database, make sure that you has some data exemples to populate your database.

# Documentation 

[books-list-api](https://books-list-api.herokuapp.com/)

## Authors import

```bash
$ python manage.py import_authors authors.csv
```
If you are having any trouble, you can run this code for help:

```bash
$ python manage.py import_authors --help
```
