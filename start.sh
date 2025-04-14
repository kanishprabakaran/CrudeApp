#!/bin/bash

# Activate virtual environment if exists
if [ -d "venv" ]; then
  source venv/bin/activate
fi

# Run the Flask app with Gunicorn
exec gunicorn -w 4 -b 0.0.0.0:8000 app:app