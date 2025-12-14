from calculate_primes import write_primes
import sys
import os

def run():
    if len(sys.argv) != 2:
        print("Usage: python3 write_new_primes.py file_path")
        print(f"{len(sys.argv)} arguments given")
        return 1

    else:
        file_path = sys.argv[-1]
        while os.path.getsize(file_path) <= 1_000_000_000:
            write_primes(file_path)
        print(f"Stopping so file doesn't get too big")

run()


