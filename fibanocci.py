def fibonacci(n):
  """
  Calculates the n-th Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate (starting from 0).

  Returns:
    The n-th Fibonacci number.
  """
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b

# Get input from the user
num = int(input("Enter the index of the Fibonacci number you want to calculate: "))

# Calculate the Fibonacci number and print the result
result = fibonacci(num)
print("The", num, "th Fibonacci number is:", result)