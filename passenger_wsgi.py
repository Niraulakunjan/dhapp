import sys
import os

# Add the current directory to the path so app.py can be found
sys.path.append(os.getcwd())

# Import the Flask app instance
from app import app as application

# Passenger expects the entry point to be called 'application'
