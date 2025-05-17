# Baby Tools World

This repository contains the source code of the 'Baby Tools World' which is a simple full stack shop application written in Python using Django 5.
The project was developed for educational purposes only and therefore has no claim to feature completeness, or only minimal claims regarding application security, user experience, or design

## Prerequisites

In order to seamlessly interact with the repository and the software it contains you need to following tools preinstalled:

- Python Interpreter
- OCI-Compliant Container Engine (e.g. podman, docker, etc.)
- Editor/IDE of your choice (VSC, PyCharm, etc.)

## Quickstart

In order to quickly get started with the project follow these steps:

1. clone the repository
1. nagivate to the repository
1. (optional) create a virtual environment with `python -m venv my-venv`
    1. activate the virtual environment: 
        - on Windows run: `my-venv/Scripts/activate`
        - on MacOS/Linux run: `source my-venv/bin/activate`
1. install the project dependencies with `pip install -r requirements.txt`
1. configure required application environment variables
    - `cp example.env .env`
1. prepare the database (create and apply migrations)
    1. `python manage.py makemigrations`
    1. `python manage.py migrate`
1. start the application with `python manage.py runserver`
1. verify the application is running by visiting `localhost:8000`