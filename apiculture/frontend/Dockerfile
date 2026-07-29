FROM python:3.11-slim

WORKDIR /app

# Copie des sources
COPY index.html .
COPY ./js ./js
COPY ./css ./css
COPY ./img ./img
COPY ./html ./html

#Sert la page sur 80
CMD ["python", "-m", "http.server", "80"]