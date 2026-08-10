"""
Searching a list Algorithm
"""
import random

numbers = []

def append_list():
    i = 0
    while i < 10:
        numbers.append(random.randint(1, 100))
        i += 1

def search(num):
    i = 0
    n = len(numbers)
    while i < n:
        if num == numbers[i]:
            return i
        else:
            i += 1

def print_list():
    for n in numbers:
        print(n)

def get_target(target):
    # Search for two numbers in numbers that add up to target
    i = 0
    n = len(numbers)
    target_found = False
    while i < n:
        a = target - numbers[i]
        q = search(a)
        if q != None and q != i:
            target_found = True
            return [numbers[i], numbers[q]]
        else:
            i += 1

        return [a, q]
        
    ...

if __name__ == "__main__":
    append_list()
    print("\nPrinting List-- ")
    print_list()
    print("\n-- Searching Algorithm --")
    n = int(input("\nEnter number to search: "))
    num = search(n)
    print(f"The index of {numbers[num]} is: {num}")
    target = int(input("Enter Target Number: "))
    nums = get_target(target)
    print(f"numbers that add to{target} are: {nums[0]} and {nums[1]}")

