# Dockerfile pentru aplicația principală
FROM python:3.9-slim

# Setăm directorul de lucru
WORKDIR /app

# Copiem fișierele din directorul local în container
COPY . /app

# Instalăm Flask și requests
RUN pip install --no-cache-dir flask requests

# Expunem portul pe care aplicația Flask va asculta
EXPOSE 5000

# Comanda care va porni aplicația
CMD ["python", "app.py"]