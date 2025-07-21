import sys
import subprocess
from pathlib import Path

solution = b"\xbf\xd2\x2f\xdc\x7c\xb1\x09\xfa\xf7\x30\x6d\x1d"

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
    