import sys
from functions.calculate_primes import *


def write_file(file_path, generate_function, check_function):

    #First we go through and check that everything previously input is correct
    line_text = ""
    line_number = 1
    with open(file_path, "r") as read_file:
        for line in read_file:
            last_line = line
            if check_function(line_number, line_text):
                pass #all is well
            else:
                raise Exception(f"There is something wrong on line {line_number}")
            line_number += 1

    #Then we can use the line number and line text saved from the earlier check to 
    # continue adding new lines to the file
    with open(file_path, "w") as write_file:
        for i in range(1_000):  # Figure out how to use a while loop that checks 
                                # the file size
            write_file.write(generate_function(line_number, line_text))
    
    print("Done for now")

