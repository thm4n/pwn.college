import requests
import subprocess
from pathlib import Path

host = "http://challenge.localhost:80"

def solve():
    headers = {
        "Host": "challenge.localhost:80",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    req = requests.get(f"{host}", headers=headers)
    print(req.text)


if __name__ == "__main__":
    solve()
