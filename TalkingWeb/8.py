import requests
import subprocess
from pathlib import Path

host = "http://challenge.localhost:80"

def solve():
    req = requests.get(f"{host}/gate")
    print(req.text)


def start_server():
    exec_path: Path = Path("/challenge/server")
    if exec_path.exists():
        subprocess.Popen(['/challenge/server'])
    else:
        print(f"no exec: {exec_path}")


if __name__ == "__main__":
    # start_server()
    solve()
