
#Imagen inicial
FROM python:3.8-slim-buster

#instalando dependencais
RUN apt update -y && apt install awscli -y

#creando el directorio app
WORKDIR /app

#copiando todos los archivos de src a la carpeta app
COPY . /app
#ejecutando los requiremnts
RUN pip install -r requirements.txt

#ejecutando la app
CMD ["python3", "app.py"]