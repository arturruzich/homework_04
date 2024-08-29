

class Student:

    def __init__(self, first_name, last_name, age, average_mark):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_mark = average_mark

    def change_average_mark(self, new_mark):
        self.average_mark = new_mark

    def student_info(self):
        print(f"Name: {self.first_name}")
        print(f"Surname: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Average mark: {self.average_mark}")


Student = Student("Artur", "Ruzich", 23, 87)

Student.student_info()

Student.change_average_mark(93)

print("\nAfter change of average mark")
Student.student_info()