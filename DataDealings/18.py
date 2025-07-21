import subprocess
import base64
from pathlib import Path


def encode_to_bits(s):
    return b"".join(format(c, "08b").encode("latin1") for c in s)


def manip(b: bytes):
    b = encode_to_bits(b)
    b = base64.b64encode(b)
    b = base64.b64encode(b)
    b = encode_to_bits(b)

    return b


def main():
    solution = b"\x03\x91\x10\xe1=\xb7\x10\xf3"
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
