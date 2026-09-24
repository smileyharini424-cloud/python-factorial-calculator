def calculate_factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


def main():
    try:
        number = int(input("Enter a number: "))

        if number < 0:
            print("Factorial is not defined for negative numbers.")
            return

        result = calculate_factorial(number)

        print(f"{number}! = {result}")

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
