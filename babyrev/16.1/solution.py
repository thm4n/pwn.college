import sys
import subprocess
from pathlib import Path

solution = b"\xdc\x3a\x27\xf5\xf5\x2e"

def solve(exec: Path):
    if exec.exists():
        proc = subprocess.Popen([str(exec)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        proc.stdin.write(solution)
        proc.stdin.close()

        result = proc.stdout.read()
        print(result.decode('utf-8'))
    else:
        print(f"no exec: {exec}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python solution.py <path_to_exec>")
        sys.exit(1)
    solve(Path(sys.argv[1]))

if __name__ == "__main__":
    main()
    