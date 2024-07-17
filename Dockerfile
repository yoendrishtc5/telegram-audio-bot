# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia el código fuente a la imagen de Docker
COPY . .

# Especifica el comando para ejecutar el bot
CMD ["python", "bot.py"]
