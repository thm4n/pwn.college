import subprocess
from pathlib import Path

def manip(b: bytes):
    return b.hex().encode("l1")


def main():
    solution = b"vsxoinjj"

    for i in range(4):
        solution = manip(solution)

    with open("solution", "wb") as f:
        f.write(solution)


def solve():
    exec_path: Path = Path("/challenge/runme")
    if exec_path.exists():
        result = subprocess.run(['/challenge/runme', 'solution'], capture_output=True, text=True)
        print(result.stdout)
    else:
        print(f"no exec: {exec_path}")

if __name__ == "__main__":
    main()
    solve()
