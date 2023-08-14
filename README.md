## django_blog
A blog project built on Django 4.
Implemented features:
  Authentication including OAuth 2.0 integration
  Pagination
  Full-text search
  Tagging system
  Commenting system
  Post recommendations based on similarity
  RESTful API integration
  User profiles

## Requirements
Python version 3.11.4
Django version 4.2.3

## Installation
Clone the repository: git clone https://github.com/Sancezzi/blog_project.git
Create a virtual environment: python -m venv venv
Activate the virtual environment: source venv/bin/activate (Linux) or venv\Scripts\activate (Windows)
Install dependencies: pip install -r requirements.txt
Apply migrations: python manage.py migrate

## Configuration
Generate keys and make changes in the .env file for authentication through Github, Google, and VK.

## Running
Start the local server: python manage.py runserver
