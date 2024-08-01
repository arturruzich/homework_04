# Task 1
''' Порахувати кількість унікальних символів в строці.
 Якщо їх більше 10 - вивести в консоль True, інакше - False.
  Строку отримати за допомогою функції input() '''

proposed_string: str = input("Provide your string here please: ")

unique_counter: int = sum([1 for char in proposed_string if proposed_string.count(char) == 1])

unique_counter: int = 0
for char in proposed_string:
    if proposed_string.count(char) == 1:
        unique_counter += 1

if unique_counter > 10:
    print(True)
else:
    print(False)



# Task 2

''' Напишіть цикл, який буде вимагати від користувача ввести слово,
 в якому є літера "h" (враховуються як великі так і маленькі).
  Цикл не повинен завершитися, якщо користувач ввів слово без букви "h" '''

is_correct_str: bool = False

while not is_correct_str:
    provided_word: str = input("Provide your word please: ").lower()

    if provided_word.find("h") != -1:
        is_correct_str = True


# Task 3

'''Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
 Напишіть код, який свормує новий list (наприклад lst2), 
 який містить лише змінні типу стрінг, які присутні в lst1.
  Данні в лісті можуть бути будь якими'''


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

desired_list: list[int] = [item for item in lst1 if isinstance(item, str)]

for item in lst1:
    if isinstance(item, str):
        desired_list.append(item)

print(desired_list)




# Task 4
'''Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті'''

provided_list_1: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #30
provided_list_2: list[int] = [10, 11, 20, 27, 30, 33] #60


result: int = sum([integer for integer in provided_list_1 if integer % 2 == 0])

sum_result: int = 0

for integer in provided_list_2:
    if integer % 2 == 0:
        sum_result += integer

print(sum_result)
print(result)
