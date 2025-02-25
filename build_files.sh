#!/bin/bash
echo "BUILD START"
python -m pip install -r requirements.txt
python manage.py tailwind init
python manage.py tailwind install
python manage.py tailwind build
# Create the staticfiles_build directory
mkdir -p staticfiles_build
# Collect static files to the staticfiles_build directory
python manage.py collectstatic --noinput --clear --settings=web_agent.settings
# Copy all static files to staticfiles_build
cp -r staticfiles/* staticfiles_build/
echo "BUILD END"
