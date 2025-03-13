def add_two_numbers(a, b):
    return a + b

def max_of_two_numbers(a, b):
    return a if a > b else b

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

def compound_interest(principal, rate, time):
    amount = principal
    for _ in range(time):
        amount += (amount * rate / 100)
    return amount - principal

def is_armstrong_number(num):
    order = 0
    temp = num
    while temp > 0:
        temp //= 10
        order += 1
    temp = num
    sum_of_powers = 0
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** order
        temp //= 10
    return sum_of_powers == num

def sum_of_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

def largest_element_in_array(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

def interchange_first_last(arr):
    if len(arr) >= 2:
        arr[0], arr[-1] = arr[-1], arr[0]
    return arr

def swap_two_elements(arr, index1, index2):
    if index1 < len(arr) and index2 < len(arr):
        arr[index1], arr[index2] = arr[index2], arr[index1]
    return arr

# Example usage
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
