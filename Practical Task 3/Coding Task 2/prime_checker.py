# prime_checker.py

def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False
    elif num <= 3:
        return True  # 2 and 3 are prime numbers
    elif num % 2 == 0 or num % 3 == 0:
        return False  # multiples of 2 and 3 are not prime
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
