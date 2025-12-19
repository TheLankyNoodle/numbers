import sys

def array_from_line(string):
    result = []
    if len(string.strip()) == 0:
        return []
    for i in string.split(","):
        result.append(int(i))
    return result

def run():
    if len(sys.argv) != 2:
        print("Usage: python3 confirm_factors.py file_path")
        print(f"{len(sys.argv)} arguments given")
        return 1
    
    file_path = sys.argv[-1]
    with open(file_path, "r") as file:
        
        problems = {}

        line_number = 1
        for line in file:
            factors = array_from_line(line)
            result = 1

            for number in factors:
                result *= number

            if result == line_number:
                pass
            else:
                problems[line_number] = factors

            line_number += 1

        if problems == {}:
            print(f"No problems found with {file_path}")
        for problem in problems:
            print(f"{problem}: {problems[problem]}")

run()



