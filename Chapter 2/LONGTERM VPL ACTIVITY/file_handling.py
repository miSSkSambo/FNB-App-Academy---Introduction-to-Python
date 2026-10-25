
OUTFILE = "calculations.txt"


def saveTextFile(multiple, valueArray, value2):
    # TODO 1: Multiply all values into a running result
    result = multiple

    for value in valueArray:
        result *= value

    # TODO 2: Check for division by zero
    if value2 == 0:
        print("Error: Cannot divide by zero. No data was saved.")
        return

    final_answer = result / value2

    # Write the results to the file without erasing previous content
    try:
        with open(OUTFILE, "a", encoding="utf-8") as file:
            file.write(f"Multiple used: {multiple}\n")
            file.write(f"Values: {valueArray}\n")
            file.write(f"Final answer: {final_answer}\n")
            file.write("-" * 30 + "\n")

        print("Results saved successfully.")

    except OSError as error:
        print(f"Error writing to file: {error}")


def readTextFile(filename):
    # TODO 3: Open and read the file
    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.readlines()

        # TODO 4: Print the contents line by line
        for line in contents:
            print(line.rstrip())

    except FileNotFoundError:
        print(f"Sorry, the file '{filename}' was not found.")

    except OSError as error:
        print(f"Error reading file: {error}")


def demo():
    multiple = 5
    valueArray = [1, 3, 5, 7]

    # First call: division by zero should not save anything
    saveTextFile(multiple, valueArray, 0)

    # TODO 5: Valid calculation and file reading
    saveTextFile(multiple, valueArray, 5)
    readTextFile(OUTFILE)


if __name__ == "__main__":
    demo()
