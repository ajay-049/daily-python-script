import math
import sys


def calculate_lcm(numbers: list[int]) -> int:
    """Calculates the Least Common Multiple (LCM) of a list of integers."""
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return math.lcm(*numbers)


def main():
    print("--- Multiple Number LCM Calculator ---")
    raw_input = input(
        "Enter integers separated by spaces (e.g., 12 18 30): "
    ).strip()

    if not raw_input:
        print("Error: No numbers entered.")
        sys.exit(1)

    try:
        # Convert input string into a list of integers
        numbers = [int(x) for x in raw_input.split()]

        # Calculate and display the result
        result = calculate_lcm(numbers)
        print(f"\nNumbers entered: {numbers}")
        print(f"Least Common Multiple (LCM): {result}")

    except ValueError:
        print("Error: Please enter valid integers only.")
        sys.exit(1)


if __name__ == "__main__":
    main()
