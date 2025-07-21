import requests
import subprocess
from pathlib import Path

host = "http://challenge.localhost:80"

def solve():
    data={
        "password": "dnhftzqm"
    }
    headers = {
        "Host": "challenge.localhost:80",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Firefox/91.0"
    }
    req = requests.post(f"{host}/check", headers=headers, data=data)
    print(req.text)


if __name__ == "__main__":
    solve()
