FROM python:3.9-slim

# Copia el directorio del servidor al contenedor
COPY ./servidor /home/app

# Establece el directorio de trabajo
WORKDIR /home/app

# Copia el archivo requirements.txt y luego instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el servidor
CMD ["python3", "server.py"]

# Path: requirements.txt