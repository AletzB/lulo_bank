#!/bin/sh
echo "Starting the application..."
python3 app/main.py 
echo "Starting the web application..."
python3 app/app.py 
exec "$@"