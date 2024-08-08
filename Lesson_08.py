#def divide (a, b):
    #try:
        #return a / b
    #except ZeroDivisionError as e:
        #print(f"Error{e}")
    #finally:
        #print("Done")


#def try_to_connect_to_db(config: dict[str, object]):
    #try:
     #   session.connect(config)
    #except ConnectionError as exception:
     #   print(exception.args)
    #finally:
     #   session.close()



#def divide_numbers(a, b):
    #try:
     #   result = a / b
   # except ZeroDivisionError:
  #      #print(f"Помилка: Ділення на нуль. {exception}")
   # except Exception as exception:
    #    print(f"We've been reised by next exception: {exception}")
    #else:
     #   print(f"Результат ділення {a} на {b}: {result}")
    #finally:
     #   print("Our program is done...")


#divide_numbers(10, 2)
#divide_numbers(5, 0)

#def check_age(age):
  #  if age < 0:
 #       raise ValueError("Вік не може бути від'ємним")

#try:
    #user_age = int(input("Введіть ваш вік: "))
   # check_age(user_age)
  #  print(f"Ваш вік: {user_age}")
#except ValueError as ve:
 #   print(f"Помилка: {ve}")

#class TooLargeValueError(Exception):
    #def __init__(self, value, limit):
       # self.value = value
       # self.limit = limit
       # message = f"Значення {value} перевищує ліміт {limit}"
       # super().__init__(message)

# Приклад використання власного виключення
#try:
   # limit = 100
   # user_input = int(input("Введіть число: "))

   # if user_input > limit:
  #      raise TooLargeValueError(user_input, limit)
 #   else:
        #print("Дякую! Ви ввели припустиме значення.")
#except TooLargeValueError as e:
 #   print(f"Помилка: {e}")
#except ValueError:
  #  print("Помилка: Будь ласка, введіть ціле число.")


#class TooLargeValueError(Exception):
    #def __init__(self, value, limit):
        #self.value = value
       # self.limit = limit
      #  message = f"Значення {value} перевищує ліміт {limit}"
     #   super().__init__(message)

# Приклад використання власного виключення
#try:
    #limit = 100
    #user_input = int(input("Введіть число: "))

    #if user_input > limit:
   #     raise TooLargeValueError(user_input, limit)
  #  else:
 #       print("Дякую! Ви ввели припустиме значення.")
#except TooLargeValueError as e:
 #   print(f"Помилка: {e}")
#except ValueError:
    #print("Помилка: Будь ласка, введіть ціле число.")


file = None
try:
    # Відкриття файлу для читання
    file = open("example.txt", "r")

    # Операції змістом файлу
    content = file.read()
except Exception as e:  # Вловлювання помилки та збереження її у змінну e
    print(f"Виникла помилка: {e}")
finally:
    # Закриття файлу у блоку finally, щоб гарантувати його виклик навіть якщо виникає помилка
    if file is not None:
        file.close()