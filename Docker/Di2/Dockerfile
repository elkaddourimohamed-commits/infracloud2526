# Dockerfile pour examen stable
FROM python:3.8.18-slim-bullseye

# Installer dépendances système
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Installer Flask
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir flask==2.2.5

# Définir le répertoire de travail dans le container
WORKDIR /home/myapp

# Copier fichiers
COPY myapp.py .
COPY templates templates
COPY static static

# Exposer la port 8080
EXPOSE 8080

# Démarrer Flask
CMD ["python3", "myapp.py"]
