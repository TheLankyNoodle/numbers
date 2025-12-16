import math
import os

def prep_file(path):
    with open(path, "r") as file:
        content = file.read()
        start_len = len(content) #only write the file again if the content is changed

        #add a couple of primes if there are none
        if len(content) < 4:
            content = "2\n3\n5"
            print("prep_file: adding first three primes")

        #remove trailing newline (if there is one)
        if content[-1] == '\n':
            content = content[:-1]
            print("prep_file: removing trailing newline")

        if len(content) != start_len:
            with open(path, "w") as file:
                file.write(content)
                print("prep_file: writing file with changes")

def proper_prime(number):
    #NOTE: This is a proper prime number checker, that doesn't use the previously known primes to check.

    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def quick_prime(number, known_primes = []):
    #NOTE: This is not a true is_prime function, it doesnt check for 0,1,2 because it assumes the file has been prepped to include 2,3,5 as the first primes
    if number % 2 == 0:
        return False
    #TODO: I should only check prime divisors
    for i in range(3, math.ceil(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

def write_primes(file_path):
    #NOTE: rough file size will be smaller than final size
    prep_file(file_path)
    with open(file_path, 'r') as file:
        content = file.read()
        largest_prime_so_far = int(content.split('\n')[-1])
     
    with open(file_path, 'a') as file:
        for i in range(largest_prime_so_far + 2, largest_prime_so_far + 2_000_000, 2):
            if quick_prime(i):
                #print(f"{i} is prime")
                file.write(f"\n{i}")
                i += 2
            #print(f"new primes written to {file_path}")
        print(f"{file_path} has {os.path.getsize(file_path)} bytes written to it")

