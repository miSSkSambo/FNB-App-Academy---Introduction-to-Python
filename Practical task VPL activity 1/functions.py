
# =====================================================================
#  PRACTICAL: DEFINING AND USING FUNCTIONS
# =====================================================================
#  Complete every function marked with a TODO.
#
#  RULES:
#   1. Do NOT change the function names or their parameters.
#   2. Do NOT change any code below the "DO NOT MODIFY" line.
#   3. Your functions must RETURN values, not print them.
#      The main() function does all the printing for you.
# =====================================================================


def greet(name):
    """
    Return a greeting of the form:  Hello, <name>!

    Example:
        greet("Thabo")  ->  "Hello, Thabo!"
    """
    return f"Hello, {name}!"


def rectangle_area(length, width):
    """
    Return the area of a rectangle.

    Example:
        rectangle_area(5, 4)  ->  20.0
    """
    return float(length * width)


def is_even(number):
    """
    Return True if number is even, and False if it is odd.

    Hint: the modulus operator (%) gives you the remainder.

    Example:
        is_even(12)  ->  True
        is_even(7)   ->  False
    """
    return number % 2 == 0


def count_vowels(text):
    """
    Return how many vowels (a, e, i, o, u) appear in text.
    Upper case and lower case vowels both count.

    Example:
        count_vowels("Programming is fun")  ->  5
    """
    count = 0
    for character in text.lower():
        if character in "aeiou":
            count += 1
    return count


def factorial(n):
    """
    Return n factorial (n!), i.e. n * (n-1) * (n-2) * ... * 1
    By definition, factorial(0) is 1.

    Example:
        factorial(5)  ->  120
    """
    result = 1
    for number in range(2, n + 1):
        result *= number
    return result


def apply_discount(price, percentage=10):
    """
    Return the price after subtracting the given percentage.
    'percentage' is a DEFAULT PARAMETER: when the caller leaves it out,
    a 10% discount must be applied.
    Round the answer to 2 decimal places.

    Example:
        apply_discount(200)      ->  180.0
        apply_discount(250, 20)  ->  200.0
    """
    return round(price * (1 - percentage / 100), 2)


# =====================================================================
#  DO NOT MODIFY ANYTHING BELOW THIS LINE
# =====================================================================
def main():
    command = input().strip().lower()

    if command == "greet":
        print(greet(input().strip()))
    elif command == "area":
        print(rectangle_area(float(input()), float(input())))
    elif command == "even":
        print(is_even(int(input())))
    elif command == "vowels":
        print(count_vowels(input()))
    elif command == "factorial":
        print(factorial(int(input())))
    elif command == "discount":
        print(apply_discount(float(input())))
    elif command == "discount_custom":
        print(apply_discount(float(input()), float(input())))
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
