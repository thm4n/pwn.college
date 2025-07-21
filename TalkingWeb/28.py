import requests

host = "http://challenge.localhost:80"

def solve():
    headers = {
        "Host": "challenge.localhost:80",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    req = requests.get(f"{host}", headers=headers)
    cookies = req.cookies.get_dict()
    print(f"Cookies: {cookies}")
    req = requests.get(f"{host}", headers=headers, cookies=cookies)
    print(req.text)


if __name__ == "__main__":
    solve()
