import random

numbers = []
numbers_replica = []
sorted_numbers = []

def append_numbers():
    i = 0
    while i < 10:
        n = random.randint(1, 100)
        numbers.append(n)
        numbers_replica.append(n)
        i += 1

def print_list():
    for n in numbers:
        print(n)

def get_smallest(numbers: list):
    i = 0
    smallest = numbers[0]
    while i < 10:
        if smallest <= numbers[i]:
            i += 1
        else:
            smallest = numbers[i]
            i += 1
    return smallest

def remove_index(a: int, numbers: list):
    i = 0
    while i < 10:
        if numbers[i] == a:
            del numbers[i]
            break
        else:
            i += 1

def sort_numbers(numbers: list):
    a = get_smallest(numbers)
    sorted_numbers.append(a)
    remove_index(a, numbers)
    i = 0
    while i < 0:
        b = get_smallest(numbers)
        sorted_numbers.append(b)
        remove_index(b, numbers)
        i += 1

        
if __name__ == "__main__":
    append_numbers()
    print("\n -- List of Numbers -- ")
    print(numbers)
    print(f"Smallest number is: {get_smallest(numbers)}")
    print(f"\nSorted List --")
    sort_numbers(numbers)
    print(sorted_numbers)
    print(numbers)
