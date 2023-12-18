# Django REST API

A Django REST Framework (DRF) project that serves as an example RESTful API.

## Features

- User authentication
- CRUD operations on resources

## Technologies Used

- Django
- Django REST Framework
- SQLite (or your preferred database)

## Getting Started

### Prerequisites

Make sure you have the following software installed:

- Python: [Download](https://www.python.org/downloads/)
- pip (Python package manager): Included with Python installation
- Django: Install using `pip install django`
- Django REST Framework: Install using `pip install djangorestframework`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bradrody24/pzaz_backend.git
   ```
2. Install the requirements and set up the shell:

   ```bash
   pipenv install
   pipenv shell
   pipenv --venv
   ```
3. Run the django app

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

