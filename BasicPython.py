import math

def add_two_numbers(a, b):
    return a + b

def max_of_two_numbers(a, b):
    return max(a, b)

def factorial(n):
    return math.factorial(n)

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    return principal * (pow((1 + rate / 100), time)) - principal

def is_armstrong_number(num):
    order = len(str(num))
    sum_of_powers = sum(int(digit) ** order for digit in str(num))
    return sum_of_powers == num

def sum_of_array(arr):
    return sum(arr)

def largest_element_in_array(arr):
    return max(arr)

def interchange_first_last(arr):
    if len(arr) >= 2:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr

def swap_two_elements(arr, index1, index2):
    if index1 < len(arr) and index2 < len(arr):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr

print("Addition:", add_two_numbers(5, 3))
print("Maximum:", max_of_two_numbers(10, 20))
print("Factorial:", factorial(5))
print("Simple Interest:", simple_interest(1000, 5, 2))
print("Compound Interest:", compound_interest(1000, 5, 2))
print("Armstrong Check (153):", is_armstrong_number(153))
print("Sum of Array:", sum_of_array([1, 2, 3, 4, 5]))
print("Largest Element:", largest_element_in_array([10, 20, 30, 40]))
print("Interchanged List:", interchange_first_last([1, 2, 3, 4, 5]))
print("Swapped List:", swap_two_elements([1, 2, 3, 4, 5], 1, 3))
