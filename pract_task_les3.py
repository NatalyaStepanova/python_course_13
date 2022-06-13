# Task 1
def div(num_1, num_2):
    try:
        return str(round(num_1 / num_2, 2))
    except ZeroDivisionError:
        return "you cant divide by zero"

numbers = input("Enter 2 numbers separated with space: ").split()
try:
    ans = div(float(numbers[0]), float(numbers[1]))
except ValueError:
    ans = "wrong arguments"

print(f"Your answer is: {ans}")

# Task 2
def user_data(**kwargs):
    ans = ""
    for i in kwargs:
        ans += i.replace("_", " ") + ": " + kwargs[i] + "\n"
    return ans

name = input("Enter name: ")
surname = input("Enter surname: ")
year_of_birth = input("Enter the year when you were born: ")
user_info = user_data(name=name, surname=surname, year_of_birth=year_of_birth)
print(f"Here's your personal info:\n{user_info}")

# Task 3
def my_func(num1, num2, num3):
    numbers = [num1, num2, num3]
    try:
        for i, elem in enumerate(numbers):
            numbers[i] = int(elem)
    except ValueError:
        return "sorry, wrong arguments"
    ind = numbers.index(min(numbers))
    numbers.pop(ind)
    summa = sum(numbers)
    return summa

user_numbers = input("Enter 3 numbers separated with space: ").split()
ans = my_func(user_numbers[0], user_numbers[1], user_numbers[2])
print(f"Your answer is: {ans}")

# Task 4
def my_func_1(x, y):
    if x < 0 or y > 0:
        return
    else:
        return x ** y

def my_func_2(x, y):
    if x < 0 or y > 0:
        return
    else:
        b = x
        if abs(y) == 1:
            return 1 / b
        for i in range(1, abs(y)):
            b = b * x
        return 1 / b

def main_func(arr, func):
    try:
        ans = func(float(numbers[0]), int(numbers[1]))
        try:
            ans = str(round(ans, 5))
        except TypeError:
            ans = "wrong arguments"
    except ValueError:
        ans = "wrong arguments"
    return ans

numbers = input("Enter 2 numbers separated with space: ").split()
str4ans = main_func(numbers, my_func_1)
print(f"Here's your answer with func 1: {str4ans}")
str4ans = main_func(numbers, my_func_2)
print(f"Here's your answer with func 2: {str4ans}")

# Task 5
# вероятно, неправильно поняла задание: не придумала, как сделать через функцию
a = False
total_sum = 0
while a == False:
    raw_numbers = input("Enter numbers separated with space. If you enter 'q' the program will stop: ").split()
    a = "q" in raw_numbers
    for i in raw_numbers:
        try:
            i = int(i)
            total_sum += i
        except ValueError:
            continue
    print(total_sum)

# Task 6, 7
def int_func(my_list):
    for ind, el in enumerate(my_list):
        my_list[ind] = el.title()
    return " ".join(my_list)

in_words = input("Enter wrods separated by space: ").split()
out_words = int_func(in_words)
print(out_words)
