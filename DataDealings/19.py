import subprocess
import base64
from pathlib import Path


def manip(b: bytes):
    b = b[::-1]
    b = base64.b64encode(b)
    b = b.hex().encode("l1")
    b = base64.b64encode(b)

    b = b.hex().encode("l1")
    b = base64.b64encode(b)
    return b


def main():
    solution = b"\x15\xe8p\x17\xe6\x0f7t"
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


"""
input = ??
pass = 3

input = (input + 5) * 3    # 3(x + 5)
pass = (pass * 7) - 5      # pass = 16

if input == pass:          # input == (((pass * 7) - 15) / 3) - 5 
    print("You win!")
"""