class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lector(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

        self.grades = {}

    # print(student1 == student2)
    def __eq__(self, other):  # ==
        return self.average_rating() == other.average_rating()

    # print(student1 != student2)
    def __ne__(self, other):  # !=
        return self.average_rating() != other.average_rating()

    # print(student1 < student2)
    def __lt__(self, other):  # <
        return self.average_rating() < other.average_rating()

    # print(student1 > student2)
    def __gt__(self, other):  # >
        return self.average_rating() > other.average_rating()

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_rating()}\n'

    def average_rating(self):
        summa = 0
        amount = 0
        for grades in self.grades.values():
            summa += sum(grades)
            amount += len(grades)

        return round(summa/amount, 2)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades.update([(course, [grade])])
        else:
            print('Ошибка ввода')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_rating()}\n' \
               f'Курсы в процессе изучения: {self.courses_in_progress}\n' \
               f'Завершенные курсы: {self.finished_courses}'

    # print(student1 == student2)
    def __eq__(self, other):  # ==
        return self.average_rating() == other.average_rating()

    # print(student1 != student2)
    def __ne__(self, other):  # !=
        return self.average_rating() != other.average_rating()

    # print(student1 < student2)
    def __lt__(self, other):  # <
        return self.average_rating() < other.average_rating()

    # print(student1 > student2)
    def __gt__(self, other):  # >
        return self.average_rating() > other.average_rating()

    def average_rating(self):
        summa = 0
        amount = 0
        for grades in self.grades.values():
            summa += sum(grades)
            amount += len(grades)

        return round(summa/amount, 2)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lector) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course].append(grade)
            else:
                lector.grades.update([(course, [grade])])
        else:
            print('Ошибка ввода')


def average_rating(persons, course):
    summa = 0
    amount = 0
    for person in persons:
        summa += sum(person.grades[course])
        amount += len(person.grades[course])

    return round(summa / amount, 2)


# 1 student
student1 = Student('Elon', 'Mask', 'male')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Git']
student1.finished_courses += ['Основы программирования']

# 2 student
student2 = Student('Mark', 'Zuckerberg', 'male')
student2.courses_in_progress += ['JavaScript']
student2.courses_in_progress += ['Html5']
student2.courses_in_progress += ['Git']
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Основы программирования']

# 1 lector
python_lector = Lector('Jhon', 'Smith')
python_lector.courses_attached += ['Python']
python_lector.courses_attached += ['Git']

# 2 lector
web_lector = Lector('Mike', 'Tyson')
web_lector.courses_attached += ['JavaScript']
web_lector.courses_attached += ['Html5']
web_lector.courses_attached += ['Python']

# 1 reviewer
python_reviewer = Reviewer('Guido', 'van Rossum')
python_reviewer.courses_attached += ['Python']
python_reviewer.courses_attached += ['Git']

# 2 reviewer
web_reviewer = Reviewer('Lou', 'Montulli')
web_reviewer.courses_attached += ['JavaScript']
web_reviewer.courses_attached += ['Html5']

# Добавление оценок
python_reviewer.rate_student(student1, 'Python', 5)
python_reviewer.rate_student(student1, 'Python', 4)

web_reviewer.rate_student(student2, 'Html5', 5)
python_reviewer.rate_student(student1, 'Git', 5)
python_reviewer.rate_student(student1, 'Git', 3)
python_reviewer.rate_student(student2, 'Git', 4)
python_reviewer.rate_student(student2, 'Git', 4)

student1.rate_lector(python_lector, 'Python', 5)

student2.rate_lector(web_lector, 'JavaScript', 4)
student2.rate_lector(web_lector, 'Html5', 4)
student2.rate_lector(web_lector, 'Python', 4)

# Перегрузка метода __str__

# print(student1)
# print(python_lector)
# print(web_reviewer)

# Перегрузка операторов сравнения
# print(student1 != student2)
# print(student1 == student1)
# print(student1.average_rating(), student2.average_rating())
# print(student1 < student2)
# print(student1 > student2)
# print(student1 != student2)
# print(python_lector.average_rating(), web_lector.average_rating())
# print(python_lector < web_lector)

print(average_rating([student1, student2], 'Git'))
print(average_rating([python_lector, web_lector], 'Python'))
