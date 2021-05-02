#!/usr/bin/env bash

# Goes inside the parent directory
cd image-repository

# Installs all the dependencies 
pip3 install -r requirements.txt

# Goes inside the Django Project and starts the server
cd imageRepo

# Create a superuser 
python3 manage.py createsuperuser

# Spin up the server
python3 manage.py runserver