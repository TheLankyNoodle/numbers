
def get_prime_factors(number, memofile = ""):
    #TODO: Should memoise, if I store a prime factors dict, then after every division I can check it and potentially save a lot of calculations

    prime_memos = {}
    if len(memofile) > 0:
        with open(memofile, "r") as file:
            n = 2
            for line in file:
                prime_memos[n] = tuple(map(lambda x: int(x), line.split(", ")))
                n += 1
    
    prime_factors = []
    number_before_divisions = number
    with open("saved_data/primes.txt", "r") as prime_list:
        while number > 0:
            for line in prime_list:
                prime = int(line.strip())
                while number % prime == 0:
                    #print(f"{number} : {prime}")
                    prime_factors.append(prime)
                    if number == prime:
                        return (number_before_divisions, prime_factors)
                    number //= prime
            for n in prime_memos:
                if number % n == 0:
                    for i in prime_memos[n]:
                        prime_factors.append(i)
                        if number == n:
                            return (number_before_divisions, prime_factors)
                        number //= n

    print("get_prime_factors: we got here")
    return (number_before_divisions, prime_factors)
