import requests

host = "http://challenge.localhost:80"

def solve():
    headers = {
        "Host": "challenge.localhost:80",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    session = requests.Session()

    req = session.get(f"{host}", headers=headers)
    print(req.content)
    req = session.get(f"{host}", headers=headers)
    print(req.content)
    req = session.get(f"{host}", headers=headers)
    print(req.content)
    req = session.get(f"{host}", headers=headers)
    print(req.content)


if __name__ == "__main__":
    solve()
