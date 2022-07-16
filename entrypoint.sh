#!/bin/sh
echo "Starting unit tests for the api..."
pytest -rA -v
echo "Starting the application from docker..."
python3 app/tvmaze.py
echo "Starting the web application..."
python3 app/main.py  
exec "$@"