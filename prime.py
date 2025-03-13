def is_prime(n):
    if n < 2: return False
    if n < 4: return True  # Handles 2 and 3
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

try:
    num = int(input("Enter an integer: "))
    print(f"{num} is {'a prime' if is_prime(num) else 'not a prime'} number.")
except ValueError:
    print("Invalid input. Please enter an integer.")