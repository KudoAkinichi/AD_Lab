# Question 1, subpart 1: Print the multiplication table of a number provided by the user
num = int(input("Enter a number for its multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# subpart 2: Calculation of the sum of all even numbers between 1 and 100
sum_even = 0
for i in range(2, 101, 2):  # Loop through even numbers only
    sum_even += i
print(f"\nSum of all even numbers between 1 and 100: {sum_even}")

# subpart 3: Creation of a pattern using nested loops
print("\nPattern:")
for i in range(1, 6):  # Outer loop for rows
    for j in range(i):  # Inner loop for printing stars
        print("*", end="")
    print()  # Move to the next line