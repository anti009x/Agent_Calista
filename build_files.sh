#!/bin/bash
echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py tailwind init
python manage.py tailwind install
python manage.py tailwind build
python manage.py collectstatic --noinput --clear
echo "BUILD END"
