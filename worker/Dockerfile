# Dockerfile pentru worker
FROM python:3.8-slim

# Setăm directorul de lucru
WORKDIR /app

# Copiem fișierele din directorul local în container
COPY . /app

# Instalăm Flask
RUN pip install flask

# Expunem portul pe care serviciul worker va asculta
EXPOSE 5001

# Comanda care va porni aplicația worker
CMD ["python", "worker_app.py"]
