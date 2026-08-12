numbers = [3, 5, 8, 9, 13, 16, 17, 19, 25, 36, 47, 49, 50]

def search_number(num):
    left = 0
    right = len(numbers) - 1
    iterations = 0

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == num:
            return [mid, iterations]

        if numbers[mid] < num:
            print("Search last half")
            left = mid + 1
            iterations += 1
        else:
            print("first half")
            right = mid - 1
            iterations += 1
    return -1

if __name__ == "__main__":
    print("\n=== Binary Search Algorithm ===\n")
    print(numbers)
    user_input = int(input("\nEnter number to search for: "))
    i = search_number(user_input)
    print(f"Search index: {i[0]}, Iterations: {i[1]}")
    