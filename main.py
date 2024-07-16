import itertools
import time

def is_solution(words, result, mapping, operation):
    words_int = [int(''.join(str(mapping[c]) for c in word)) for word in words]
    result_int = int(''.join(str(mapping[c]) for c in result))
    
    if operation == '1':  # Addition
        return sum(words_int) == result_int
    elif operation == '2':  # Subtraction
        return words_int[0] - sum(words_int[1:]) == result_int
    elif operation == '3':  # Multiplication
        prod = 1
        for num in words_int:
            prod *= num
        return prod == result_int
    elif operation == '4':  # Division
        try:
            div = words_int[0]
            for num in words_int[1:]:
                div /= num
            return div == result_int
        except ZeroDivisionError:
            return False
    return False

def solve_cryptarithm(words, result, operation):
    unique_chars = set(''.join(words) + result)
    if len(unique_chars) > 10:
        print("Too many unique characters!")
        return

    digits = '0123456789'
    for perm in itertools.permutations(digits, len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if is_solution(words, result, mapping, operation):
            print("\nSolution found!")
            for word in words:
                print(f"{word} -> {''.join(mapping[c] for c in word)}")
            print(f"{result} -> {''.join(mapping[c] for c in result)}")
            return

    print("No solution found.")

def main():
    while True:
        print("-" * 50)
        print("Cryptarithm Solver")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        choice = input("Choose an operation: ")

        if choice == '5':
            break

        if choice not in '1234':
            print("Invalid choice!")
            continue

        words = input("Enter the words (space-separated): ").split()
        result = input("Enter the result word: ")

        print("\nLoading, please wait...")
        time.sleep(2)  # Simulate loading delay

        solve_cryptarithm(words, result, choice)
        
        print("-" * 50)
        print("\nWould you like to solve another cryptarithm? (yes/no)")
        continue_choice = input().strip().lower()
        if continue_choice != 'yes':
            break
        print("\n" * 3)  # Add empty lines

if __name__ == "__main__":
    main()
