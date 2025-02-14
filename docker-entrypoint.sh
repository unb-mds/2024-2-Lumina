#!/bin/bash
# Apply database migrations
echo "Apply database migrations" 
python src/manage.py migrate 
# Start server
echo "Starting server" 
python src/manage.py runserver 0.0.0.0:8000 