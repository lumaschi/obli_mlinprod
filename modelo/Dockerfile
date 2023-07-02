FROM ubuntu:20.04

# Actualizar los repositorios
RUN sed -i 's/hirsute/focal/g' /etc/apt/sources.list && \
    apt-get update && \
    apt-get upgrade -y

# Instalar Python y pip
RUN apt-get install -y python3 python3-pip

COPY ./app /app

# Copiar el archivo del modelo al directorio de trabajo
COPY conv.h5 /app/conv.h5

# Copiar el archivo de requisitos al directorio de trabajo
COPY requirements.txt /app/requirements.txt

# Establecer el directorio de trabajo
WORKDIR /app

#Prueba para que no de time out
#RUN pip install --default-timeout=100 future 
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

# Instalar las dependencias y las versiones específicas de TensorFlow y Keras
RUN pip3 install -r requirements.txt

# Exponer el puerto 80
EXPOSE 80

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]