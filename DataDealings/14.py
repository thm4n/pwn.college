import subprocess
from pathlib import Path

SOLUTION_FILE = "lglr"

def manip(b: bytes) -> bytes:
    return b.decode("latin1").encode("utf-16")


def main():
    solution = b"yufsqaev"

    solution = manip(solution)

    with open(SOLUTION_FILE, "wb") as f:
        f.write(solution)


def solve():
    exec_path: Path = Path("/challenge/runme")
    if exec_path.exists():
        result = subprocess.run(['/challenge/runme', SOLUTION_FILE], capture_output=True, text=True)
        print(result.stdout)
    else:
        print(f"no exec: {exec_path}")

if __name__ == "__main__":
    main()
    solve()
