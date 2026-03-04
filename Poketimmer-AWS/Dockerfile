# 1. Usar una imagen oficial de Python
FROM python:3.11-slim

# 2. Configurar variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Crear directorio de trabajo
WORKDIR /app

# 4. Instalar dependencias del sistema (para PostgreSQL o librerías de imagen)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 5. Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn whitenoise  # Servidores para producción

# 6. Copiar el código del proyecto
COPY . /app/

# 7. Recolectar estáticos al construir
RUN python manage.py collectstatic --noinput

# 8. Comando para arrancar con Gunicorn (más potente que runserver)
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]