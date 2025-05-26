# Baby Tools World

This repository contains the source code of the 'Baby Tools World' which is a simple full stack shop application written in Python using Django 5.
The project was developed for educational purposes only and therefore has no claim to feature completeness, or only minimal claims regarding application security, user experience, or design.

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
1. (optional) create a superuser by running: `python manage.py createsuperuser`

## Project Structure

- `.gitlab`: GitLab specific project files
- `.github`: GitHub specific project files
- `src`: application source code, containing the django project, apps, and other files
- `requirements.txt`: the project dependencies

### Apps Overview

The project is modularized into several apps:

- `products`: Manages product listings and categories
- `users`: Handles user authentication and registration.

Each app has its own `models.py`, `views.py`, `urls.py`, and `admin.py` files to encapsulate its functionality.


## Usage

In this section you can read about the project a bit more in detail.

### Configuration

To configure the project, follow these steps:

1. Copy the example environment file to the `src` directory: `cp example.env src/.env`.
    - the file needs to be stored next to the manage.py file in order to function properly. 
    Other locations might also work but there is no guarantuee, and in last consequence you will need to update to project correspondingly.
2. Open your `src/.env` and set the required environment variables:
    - `ALLOWED_HOSTS`: provide a list of comma-separated values for the allowed host configuration => Defaults to `'localhost, 127.0.0.1, 0.0.0.0'`
    - `DEBUG`: Set to `True` for development or `False` for production. Defaults to `True`

### Running with Gunicorn

Gunicorn is a Python WSGI HTTP server that can be used to serve the application in a production-like environment.

1. **Run the Application**:
    Use the following command to start the application with Gunicorn:
    ```bash
    gunicorn --bind 0.0.0.0:8000 baby_tool_world.wsgi:application
    ```

2. **Configuration Options**:
    You can customize Gunicorn with additional options, such as:
    - `--workers`: Number of worker processes (e.g., `--workers 3`).
    - `--timeout`: Request timeout in seconds (e.g., `--timeout 30`).

3. **Verify the Application**:
    Visit `http://localhost:8000` to ensure the application is running with Gunicorn.

By using Gunicorn, you can serve the application efficiently in a production-like setup.
