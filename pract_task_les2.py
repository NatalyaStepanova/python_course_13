# Задание 1
my_list = [2, 2.97, 'hi', True, ['apple', 'pear'], {'species': 'dog', 'name': 'Hatiko'}, (1, 2, 3, 4, 5), {'a', 'h'}]
for i in my_list:
    print(f"Тип данных {my_list.index(i) + 1}-го элемента - {type(i)}")

# Задание 2
list = input("Enter numbers with spaces: ").split()
for i in range(1, len(list), 2):
    list.insert(i - 1, list.pop(i))
print(list)

# Задание 3
seasons = {"winter": [1, 2, 12], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11]}
user_month = int(input("Enter month number: "))
for i in seasons:
    if user_month in seasons[i]:
        print(f"The season of your month is {i}")
        break
    else:
        continue

# Задание 4
user_list = input("Enter words, separated by spaces: ").split()
for i in user_list:
    print(f"{user_list.index(i) + 1}: {i[:10]}")
# вариант с enumerate
user_list = input("Enter words, separated by spaces: ").split()
for i, x in enumerate(user_list, 1):
    print(f"{i}: {x[:10]}")

# Задание 5
my_list = [7, 5, 3, 3, 2]
user_number = int(input("Enter a number: "))
my_list.append(user_number)
my_list.sort()
my_list.reverse()
print(my_list)
# вариант реализации
my_list = [7, 5, 3, 3, 2]
user_number = int(input("Enter a number: "))
index = 0
for i in my_list:
    if i < user_number:
        if my_list.index(i) > 0:
            index = my_list.index(i) - 1
        break
    elif my_list.index(i) == len(my_list) - 1:
        index = len(my_list)
my_list.insert(index, user_number)
print(my_list)

# Задание 6
goods = []
user_react = "y"
numb = 0
while user_react == "y":
    numb += 1
    itemList = []
    itemList.append(numb)
    carateristics = {}
    carateristics['название'] = input("Введите название товара: ")
    carateristics['цена'] = input("Введите стоимость товара: ")
    carateristics['количество'] = input("Введите количество товара: ")
    carateristics['ед'] = input("Введите единицу измерения товара, напр. 'шт' или 'кг': ")
    itemList.append(carateristics)
    user_react = ""
    while user_react == "":
        user_react = input("Желаете продолжить? y / n").lower()
        if user_react != "y" and user_react != "n":
            user_react = ""
            print("Я не понимаю")
    item = tuple(itemList)
    goods.append(item)
analytics = {"название": [], "цена": [], "количество": [], "ед": []}
for i in goods:
    item = i[1]
    analytics["название"].append(item["название"])
    analytics["цена"].append(item["цена"])
    analytics["количество"].append(item["количество"])
    analytics["ед"].append(item["ед"])
print(analytics)
