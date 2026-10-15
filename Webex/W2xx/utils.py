# utils.py
import requests
import json
from config import ACCESS_TOKEN, BASE_URL, LOG_FILE
from datetime import datetime
import os

# Headers pour l'API Webex
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# Fonction de logging
def log_action(message: str):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()}Z {message}\n")

# GET request
def get(endpoint, params=None):
    url = f"{BASE_URL}/{endpoint}"
    r = requests.get(url, headers=headers, params=params)
    log_action(f"GET {url} → {r.status_code}")
    try:
        return r.json()
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}

# POST request
def post(endpoint, data):
    url = f"{BASE_URL}/{endpoint}"
    r = requests.post(url, headers=headers, json=data)
    log_action(f"POST {url} → {r.status_code} | payload: {data}")
    try:
        return r.json()
    except json.JSONDecodeError:
        return {"error": "Invalid JSON response"}

# DELETE request
def delete(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    r = requests.delete(url, headers=headers)
    log_action(f"DELETE {url} → {r.status_code}")
    return r.status_code
