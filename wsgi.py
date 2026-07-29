import sys

# Add your project path here (PythonAnywhere pe yeh path hoga)
path = '/home/yourusername/databreachchecker'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
