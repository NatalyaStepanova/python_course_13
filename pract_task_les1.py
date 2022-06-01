# Задание 1
user_numb = int(input("Введите число: "))
print(f"Вот ваше число: {user_numb}. А вот оно же во второй степени: {user_numb ** 2}")
user_text = input("А теперь введите текст: ")
print("Вот ваш текст: %s" % user_text)

# Задание 2
numb_of_secs = int(input("Enter time in seconds: "))
hours = numb_of_secs // 3600
minutes = numb_of_secs % 3600 // 60
seconds = numb_of_secs % 3600 % 60
min4ans = "0" + str(minutes) if minutes // 10 == 0 else str(minutes)
secs4ans = "0" + str(seconds) if seconds // 10 == 0 else str(seconds)
print(f"Вот, что получилось: {hours}:{min4ans}:{secs4ans}")

# Задание 3
user_numb = input("Введите число: ")
numb4ans = int(user_numb) + int(user_numb * 2) + int(user_numb * 3)
print("Вот что получилось: %d" % numb4ans)

# Задание 4
user_numb = int(input("Введите целое положительное число: "))
max_numb = 0
prev_numb = 0
while user_numb != 0:
    max_numb = user_numb % 10
    if max_numb == 9:
        break
    elif max_numb < prev_numb:
        max_numb = prev_numb
    prev_numb = user_numb % 10
    user_numb = user_numb // 10
print(f"Самая большая цифра - это {max_numb}")

# Задание 5 и 6
revenue = float(input("Введите значение выручки в рублях: "))
loss = float(input("Введите значение убытков в рублях: "))
profit = revenue - loss
if profit > 0:
    print(f"Поздравляю! Вы сработали в плюс! Прибыль составила {round(profit, 2)} руб. Рентабельность выручки - {round(profit / revenue, 2)}")
    numbOfEmployee = int(input("Сколько у вас сотрудников?"))
    print(f"Прибыль в расчете на одного сотрудника составила {round(profit / numbOfEmployee, 2)} руб.")
elif profit < 0:
    print(f"Вы теряете деньги:( Чистый убыток составил {round(profit, 2)} руб.")
else:
    print("Вы сработали в ноль. Держитесь на плаву!")

# Задание 7
start_dist = float(input("Введите расстояние, которое пробежал спортсмен в первый день в км.: "))
target_dist = float(input("Введите расстояние, которое должен пробегать спортсмен в км.: "))
day = 1
i = start_dist
while i < target_dist:
    i += start_dist * 0.1
    day += 1
print(f"Начав бегать с {start_dist} км, спортсмен на {day}-й день достиг цели в {target_dist} км.")