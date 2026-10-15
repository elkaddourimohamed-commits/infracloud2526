#!/bin/bash

# Nettoyage
docker rm -f eigencontainer 2>/dev/null
rm -rf tempimage

# Controle bestanden
if [ ! -f myapp.py ]; then
  echo "❌ myapp.py niet gevonden"
  exit 1
fi

# Mappen maken
mkdir -p tempimage/templates tempimage/static

# Bestanden kopiëren
cp myapp.py tempimage/
cp -r templates/* tempimage/templates/
cp -r static/* tempimage/static/

# Dockerfile maken
cat <<EOF > tempimage/Dockerfile
FROM python:3.8-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

RUN python -m pip install --no-cache-dir --progress-bar off flask==2.2.5

WORKDIR /home/myapp
COPY myapp.py .
COPY templates templates
COPY static static

EXPOSE 8080
CMD ["python3", "myapp.py"]
EOF


# Build & run
cd tempimage || exit
docker build -t eigenimage .
docker run -d -p 8080:8080 --name eigencontainer eigenimage

docker ps
