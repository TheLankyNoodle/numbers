from functions.get_prime_factors import get_prime_factors

with open("sandwich_factors.txt", 'a') as file:
    for i in range(10, 20):
        file.write(f"\n{(get_prime_factors(int(f"1{'0'*i}1")))}")
        if i % 100 == 0:
            print('.', end = '')
