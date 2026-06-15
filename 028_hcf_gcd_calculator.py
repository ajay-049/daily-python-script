import math
import sys


def calculate_gcd(numbers: list[int]) -> int:
    """Calculates the Highest Common Factor (HCF/GCD) of a list of integers."""
    if not numbers:
        raise ValueError("The list cannot be empty.")
    return math.gcd(*numbers)


def main():
    print("--- Multiple Number HCF/GCD Calculator ---")
    raw_input = input(
        "Enter integers separated by spaces (e.g., 24 60 96): "
    ).strip()

    if not raw_input:
        print("Error: No numbers entered.")
        sys.exit(1)

    try:
        # Convert input string into a list of integers
        numbers = [int(x) for x in raw_input.split()]

        # Calculate and display the result
        result = calculate_gcd(numbers)
        print(f"\nNumbers entered: {numbers}")
        print(f"Highest Common Factor (HCF/GCD): {result}")

    except ValueError:
        print("Error: Please enter valid integers only.")
        sys.exit(1)


if __name__ == "__main__":
    main()
