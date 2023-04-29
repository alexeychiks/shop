# Online Shop

This shop is built with Django 4.x and uses an embedded SQLite3 database.

## Install

```bash
# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source ./venv/bin/activate

# Install prerequisite packages
python3 -m pip install -U pip setuptools wheel
python3 -m pip install -r requirements.txt

# If you're a developer, also install helpers...
python3 -m pip install -r requirements.dev.txt
```

Next, initialize Django.

```bash
# Run database migrations
python3 manage.py migrate

# Setup an initial administrator user
python3 manage.py createsuperuser
```

## Run

```bash
# Start a development web server
python3 manage.py runserver
```
