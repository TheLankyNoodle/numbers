
def get_prime_factors(number):
    prime_factors = []
    start_number = number
    with open("primes.txt", "r") as prime_list:
        while number > 0:
            for line in prime_list:
                prime = int(line.strip())
                while number % prime == 0:
                    #print(f"{number} : {prime}")
                    prime_factors.append(prime)
                    if number == prime:
                        return (start_number, prime_factors)
                    number //= prime
            print("Run out of primes")
    print("get_prime_factors: we got here")
    return (start_number, prime_factors)
