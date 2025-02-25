#!/bin/bash
echo "BUILD START"
python3 -m pip install -r requirements.txt
python3 manage.py tailwind init
python3 manage.py tailwind install
python3 manage.py tailwind build
python3 manage.py collectstatic --noinput --clear
echo "BUILD END"
