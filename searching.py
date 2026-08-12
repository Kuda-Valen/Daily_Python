numbers = [3, 5, 8, 9, 13, 16, 17, 19, 25, 36, 47, 49, 50]

def search_number(num):
    a = []               # this will represent the small list
    l = len(numbers)
    i = 0
    found = False
    half = l // 2
    while found == False:
        if num >= numbers[half] and num in numbers:
            if num == numbers[half]:
                print("Found")
                found = True
            else:
                found = False
        elif num <= numbers[half] and num in numbers:
            print("Seach first half")
        else:
            print("Number not found!!")

if __name__ == "__main__":
    print("\n=== Binary Search Algorithm ===\n")
    print(numbers)
    user_input = int(input("\nEnter number to search for: "))
    search_number(user_input)
    