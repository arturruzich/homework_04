# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):

    multiplier = 1

    while True:
        result = number * multiplier
        if result > 25:
            break
        print(f"{number}x{multiplier}={result}")
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_two_numbers(a, b):
    return a + b


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def average(numbers):
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse_string(s):
    return s[::-1]


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def find_longest_word(words):
    if not words:
        return ""
    return max(words, key=len)


words_list = ["QA", "Automation", "Python", "Manual", "Engineer"]
longest_word = find_longest_word(words_list)
print("The longest word is:", longest_word)


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) #

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))

# task 7


def calculate_total_sea_area(black_sea_area, azov_sea_area):

    return black_sea_area + azov_sea_area

black_sea = 436402
azov_sea = 37800
total_sea_area = calculate_total_sea_area(black_sea, azov_sea)
print(f"Total area of Black and Azov seas: {total_sea_area} km2")


# task 8


def calculate_warehouse_goods(total_goods, goods_1_2, goods_2_3):
    warehouse_2 = (goods_1_2 + goods_2_3 - total_goods) / 2
    warehouse_1 = goods_1_2 - warehouse_2
    warehouse_3 = goods_2_3 - warehouse_2
    return warehouse_1, warehouse_2, warehouse_3

total_goods = 375291
goods_1_2 = 250449
goods_2_3 = 222950
warehouses = calculate_warehouse_goods(total_goods, goods_1_2, goods_2_3)
print(f"Goods in warehouse 1: {warehouses[0]}")
print(f"Goods in warehouse 2: {warehouses[1]}")
print(f"Goods in warehouse 3: {warehouses[2]}")


# task 9


def calculate_computer_cost(monthly_payment, months):

    return monthly_payment * months

monthly_payment = 1179
months = 18
computer_cost = calculate_computer_cost(monthly_payment, months)
print(f"Total price of PC: {computer_cost} UAH")


# task 10


def calculate_order_cost(order_list):

    total_cost = sum(quantity * price for _, quantity, price in order_list)
    return total_cost


orders = [
    ("Large pizza", 4, 274),
    ("Middle pizza", 2, 218),
    ("Juice", 4, 35),
    ("Cake", 1, 350),
    ("Water", 3, 21)
]
order_cost = calculate_order_cost(orders)
print(f"Total price: {order_cost} UAH")


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""