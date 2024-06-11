import json
from datetime import datetime

import requests


def main():
    url = "http://0.0.0.0:8001/contacts"
    current_datetime = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": 1,
        "email": "test@test.com",
        "url": "https://example.com/",
        "gender": 1,
        "message": "test",
        "is_enabled": True,
        "created_at": current_datetime,
    }

    res = requests.post(url, json.dumps(body))
    if res.status_code == 200:
        print(res.json())
    else:
        print(f"{res.status_code} error: {res.text}")


if __name__ == "__main__":
    main()
