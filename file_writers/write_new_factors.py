from functions.get_prime_factors import get_prime_factors

def length_of_file():
    with open("saved_data/prime_factors.txt", "r") as file:
        return sum(1 for line in file)

with open("saved_data/prime_factors.txt", "a") as file:
    for count in range(120):
        start = length_of_file() + 1
        print(start)
        for i in range(start, start + 10_000):
            factors = ", ".join(map(lambda x: str(x), get_prime_factors(i)[1]))
            file.write(f"{factors}\n")

print(length_of_file())
