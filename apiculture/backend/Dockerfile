FROM python:3.13
WORKDIR /usr/local/app

# Installation des dependances
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copie des sources
COPY src ./src
COPY main.py main.py

# Deploiement sur 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]