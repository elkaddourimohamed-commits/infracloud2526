import os
import requests
from dotenv import load_dotenv

def main():
    load_dotenv()

    api_url = os.getenv("API_URL")
    timeout = int(os.getenv("REQUEST_TIMEOUT", "5"))

    response = requests.get(api_url, timeout=timeout)

    print("HTTP status:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))

    json_data = response.json()
    print("Aantal keys in response:", len(json_data))

if __name__ == "__main__":
    main()

    
print("API_URL =", api_url)
