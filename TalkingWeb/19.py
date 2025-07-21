import requests
import subprocess
from pathlib import Path

host = "http://challenge.localhost:80"

def solve():
    data={
        "challenge_key": "bxfzwxzl"
    }
    headers = {
        "Host": "challenge.localhost:80",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    req = requests.post(f"{host}/hack", headers=headers, data=data)
    print(req.text)


if __name__ == "__main__":
    solve()
