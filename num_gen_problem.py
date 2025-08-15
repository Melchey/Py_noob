"""
Py problem: 
> Create a random generator thaat generates from 1-n.
> Store the generated numbers in a JSON file.
> Generated values cannot be repeated.
> The generator reads from the file before genearating.
> Stops with the word 'LIMIT HIT' when a total of n-unique values 
  has been generated within the defined limits.
> Prints the content of the JSON file.
"""

# Solution
import json
import random
import os

def load_numbers(filename):
    if os.path.exists(filename):
         with open(filename, 'r') as file:
            return json.load(file)
    return []
    
def save_numbers(numbers, filename):
    with open(filename, 'w') as file:
        json.dump(numbers, file)

def gen_unique_num(numbers):
    while True:
        number = random.randint(1, 500)
        if number not in numbers:
            return number
    
def main():
    filename = 'numbers.json'
    numbers = load_numbers(filename)

    while len(numbers) < 1000:
        new_number = gen_unique_num(numbers)
        numbers.append(new_number)
        save_numbers(numbers, filename)
        print(f"GENERATED NUMBER: {new_number}")

    if len(numbers) == 500:
        print("\nLIMIT HIT")
        # print the content of the JSON file
        print("\nJSON file contents: ")
        for num in numbers:
            print(f"\n{num}")

if __name__ == "__main__":
    main()



