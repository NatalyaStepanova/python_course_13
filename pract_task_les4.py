# Task 1
from sys import argv
name, hours, rate, bonus = argv
def wages(n_1, n_2, n_3):
    try:
        result = float(argv[1]) * float(argv[2]) + float(argv[3])
        print(f"Your wages is: {result}")
    except ValueError:
        print("Sorry, wrong arguments")

wages(hours, rate, bonus)

# Task 2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [n for n in my_list if my_list.index(n) - 1 >= 0 and n > my_list[my_list.index(n) - 1]]
print(new_list)

# Task 3
my_list = [n for n in list(range(20, 240)) if n % 20 == 0 or n % 21 == 0]
print(my_list)

# Task 4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [n for n in my_list if my_list.count(n) == 1]
print(new_list)

# Task 5
from functools import reduce
my_list = [n for n in range(100, 1001) if n % 2 == 0]
def mult(n_1, n_2):
    return n_1 * n_2
result = reduce(mult, my_list)
print(result)

# Task 6
from itertools import count
generator_values = []
k = 1
for i in count(10):
    if k < 11:
        generator_values.append(i)
        k += 1
    else:
        break
print(generator_values)

from itertools import cycle
generator_values = []
k = 1
for i in cycle([1, 2, 3]):
    if k < 11:
        generator_values.append(i)
        k += 1
    else:
        break
print(generator_values)

# Task 7
def fact(numb):
    k = 1
    for i in range(1, numb + 1):
        k = k * i
        yield k
n = int(input("Enter an integer: "))
for el in fact(n):
    print(el)

from math import factorial
def fact(numb):
    for i in range(1, numb + 1):
        yield factorial(i)
n = int(input("Enter an integer: "))
for el in fact(n):
    print(el)

