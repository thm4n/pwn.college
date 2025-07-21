import subprocess
from pathlib import Path

def manip(b: bytes):
    _b1 = b.hex()
    _b2 = _b1.encode("l1")
    return _b2[::-1]


def main():
    solution = b"\x8a\x00\x9e\xce\x00\xb8\x83R"
    solution = manip(solution)

    return solution


def solve(solution: bytes):
    exec_path: Path = Path("/challenge/runme")
    if exec_path.exists():
        proc = subprocess.Popen(['/challenge/runme'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        proc.stdin.write(solution)
        proc.stdin.close()

        result = proc.stdout.read()
        print(result.decode('utf-8'))
    else:
        print(f"no exec: {exec_path}")


if __name__ == "__main__":
    solution = main()
    solve(solution)
