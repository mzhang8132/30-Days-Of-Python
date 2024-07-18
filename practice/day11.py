# Day 11: 30 Days of python programming

def add_two_numbers(x, y):
    return x + y

def area_of_circle(r):
    return 3.14 * r * r

def add_all_nums(*nums):
    if all(isinstance(num, (float, int)) for num in nums):
        return sum(nums)
    else:
        return "Error: not all values are numeric"
    
def convert_celsius_to_fahrenheit(temp):
    return (temp * 9 / 5) + 32

def check_season(month):
    autumn = ["September, October, November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    if month in autumn:
        return "Autumn"
    elif month in winter:
        return "Winter"
    elif month in spring:
        return "Spring"
    else:
        return "Summer"
    
def calulate_slope(x1, x2, y1, y2):
    return (y1 - y2) / (x1 - x2)

def solve_quadratic_eqn():
    pass

def print_list(arr):
    for i in arr:
        print(i)

def reverse_list(arr):
    rev_arr = []
    for i in range(len(arr) - 1, -1, -1):
        rev_arr.append(arr[i])
    return rev_arr

def capitalize_list_items(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].upper()
    return arr

def add_item(arr, item):
    return arr + [item]

def remove_item(arr, item):
    index = arr.index(item)
    if index < len(arr) - 1:
        return arr[:index] + arr[index + 1:]
    else:
        return arr[:index]
    
def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

def sum_of_odds(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 != 0:
            sum += i
    return sum

def sum_of_even(num):
    sum = 0
    for i in range(num + 1):
        if i % 2 == 0:
            sum += i
    return sum

def even_and_odds(num):
    even = 0
    odd = 0
    for i in range(num + 1):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"# The number of odds are {odd}.\n# The number of evens are {even}."

def factorial(num):
    result = 1
    for i in range(num + 1):
        if i == 0:
            continue
        result *= i
    return result

def is_empty(arr):
    if len(arr) == 0:
        return True
    else:
        return False
    
def calulate_mean(arr):
    return sum(arr) / len(arr)

def calculate_median(arr):
    arr.sort()
    if len(arr) % 2 == 1:
        return [arr[len(arr)//2]]
    else:
        return [arr[(len(arr)//2) - 1], arr[(len(arr)//2)]]
    
def calculate_mode(arr):
    mode = arr[0]
    instances = 1
    for i in arr:
        if arr.count(i) > instances:
            instances = arr.count(i)
            mode = i
    return mode

def calculate_range(arr):
    arr.sort()
    return arr[-1] - arr[0]

def calculate_variance(arr):
    pass

def calulate_std(arr):
    pass

def is_prime(num):
    divisors = 0
    if num < 2:
        return False
    for i in range(num):
        if num % i == 0:
            divisors += 1
    if divisors > 2:
        return False
    else:
        return True
    
def unique_items(arr):
    if len(arr) == len(set(arr)):
        return True
    else:
        return False
    
