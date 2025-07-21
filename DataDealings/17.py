import subprocess
import base64
from pathlib import Path

def manip(b: bytes):
    return base64.b64encode(b)


def main():
    solution = b"\x16\xce\xbe'iB\xd5\x93"
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
