#!/bin/bash
# Running makemigrations
echo "Running makemigrations" 
docker exec lumina-web python src/manage.py makemigrations 
# Apply database migrations
echo "Apply database migrations" 
docker exec lumina-web python src/manage.py migrate 