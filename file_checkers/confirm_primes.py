from calculate_primes import proper_prime
import sys

def run():
    if len(sys.argv) != 2:
        print("Usage: python3 confirm_primes.py file_path")
        print(f"{len(sys.argv)} arguments given")
        return 1

    with open(sys.argv[-1]) as file:
        problems = []
        out_of_order = []
        previous_check = 0

        for line in file:
            line_int = int(line.strip())
            if line_int <= previous_check:
                out_of_order.append(line_int)

            if not proper_prime(line_int):
                problems.append(line)
                print(f"Found non prime: {line}")
            previous_check = line_int

        if len(problems) == 0:
            print("No problematic prime preteneders present")
        else:
            print(f"{len(problems)} false primes discovered")

        if len(out_of_order) == 0:
            print("No out of order numbers found")
        else:
            print(f"The following were smaller than the previous number:\n{out_of_order}")

run()

