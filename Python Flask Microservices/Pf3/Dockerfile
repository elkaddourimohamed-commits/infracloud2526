# Basis image
FROM python:3.11-slim

# Werkomgeving
WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Code
COPY app.py .

# Poort
EXPOSE 5050

# Start app
CMD ["python", "app.py"]
