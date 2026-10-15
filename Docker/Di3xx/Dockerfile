FROM python:3.11-slim

WORKDIR /home/myapp

COPY requirements.txt /home/myapp/

# Désactiver Rich complètement
ENV PIP_NO_PROGRESS_BAR=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DEFAULT_TIMEOUT=100
ENV PIP_USE_FEATURE=fast-deps

# Installer les dépendances directement
RUN python -m pip install --no-cache-dir --disable-pip-version-check --no-input -r requirements.txt

COPY ./static /home/myapp/static/
COPY ./templates /home/myapp/templates/
COPY app.py /home/myapp/

EXPOSE 8080
ENV PORT=8080
ENV DATA_DIR=/home/myapp/data

CMD ["python3", "/home/myapp/app.py"]
