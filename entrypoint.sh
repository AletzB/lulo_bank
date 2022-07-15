#!/bin/sh
echo "Starting the application from docker..."
python3 app/tvmaze.py
echo "Starting the web application..."
python3 app/main.py  
exec "$@"