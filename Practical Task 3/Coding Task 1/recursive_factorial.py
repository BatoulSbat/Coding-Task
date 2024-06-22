# recursive_factorial.py

def factorial(n):
    """Recursive function to calculate factorial of n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a non-negative integer to calculate its factorial: "))
    print(f"The factorial of {num} is: {factorial(num)}")
