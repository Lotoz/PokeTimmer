import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application
from waitress import serve

if __name__ == '__main__':
    application = get_wsgi_application()
    print("Iniciando Poké-Pomodoro Backend en http://127.0.0.1:8000")
    
    # Levantamos el servidor en el puerto 8000
    serve(application, host='127.0.0.1', port=8000)