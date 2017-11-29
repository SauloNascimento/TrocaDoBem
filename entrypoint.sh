#!/bin/bash

python /opt/trocadobem/manage.py makemigrations
python /opt/trocadobem/manage.py migrate
python /opt/trocadobem/manage.py runserver
