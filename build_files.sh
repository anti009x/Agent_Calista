#!/bin/bash
echo "BUILD START"
python -m pip install -r requirements.txt
npm install
python manage.py tailwind install  # (only install if needed)
python manage.py tailwind build
python manage.py collectstatic
echo "BUILD END"
