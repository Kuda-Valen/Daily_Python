"""
We want user to enter target value, and we search if there exist two numbers in our list that add to that user target
"""

import random

numbers = []

def append_numbers():
    i = 0
    while i < 10:
        numbers.append(random.randint(1, 100))
        i += 1

def search_numbers(x):
    i = 0
    while i < 10:
        if x == numbers[i]:
            return i
        else:
            i += 1

def search_target(target):
    i = 0
    while i < 10:
        a = target - numbers[i]
        b = search_numbers(a)
        if b != None and b != i:
            return [i, b]
        else:
            i += 1

if __name__ == "__main__":
    append_numbers()
    print(numbers)
    target = int(input("\nEnter target value: "))
    target_indexes = search_target(target)
    print(f"{target_indexes}")
        