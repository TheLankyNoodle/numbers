
def get_prime_factors(number):
    #TODO: Should memoise, if I store a prime factors dict, then after every division I can check it and potentially save a lot of calculations
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
            raise Exception("Run out of primes")
            #TODO: Should probably generate some more primes if we get to this point

    print("get_prime_factors: we got here")
    return (start_number, prime_factors)
