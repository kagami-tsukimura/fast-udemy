import json
from datetime import datetime

import requests


def main():
    url = "http://0.0.0.0:8001/contacts"
    current_datetime = datetime.now().isoformat()
    body = {
        "id": 1,
        "name": "test",
        "email": "test@test.com",
        "url": "https://example.com/",
        "gender": 1,
        "message": "test",
        "is_enabled": True,
        "created_at": current_datetime,
    }

    res = requests.post(url, json.dumps(body))
    print(res.json())


if __name__ == "__main__":
    main()
