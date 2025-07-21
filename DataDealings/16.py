import subprocess
import base64
from pathlib import Path

def manip(b: bytes):
    return base64.b64decode(b.decode("l1"))


def main():
    solution = b"+ROoXPZ/TAg="
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
