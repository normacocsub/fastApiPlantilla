# Utilizamos una imagen de Python 3.9 como base
FROM python:3.11

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos el archivo requirements.txt al directorio de trabajo
COPY requirements.txt .

# Instalamos las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de los archivos del proyecto al directorio de trabajo
COPY . .

# Install MySQL client
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*


# Exponemos el puerto 8000
EXPOSE 80

# Iniciamos el servidor web
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
