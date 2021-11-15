class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lec(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФмилия: {self.surname}\nСредняя оценка за ДЗ: {medium_grade(self.grades)}\n\
Курсы в процессе обучения: {", ".join(self.courses_in_progress)}\nЗаконченные курсы: \
{", ".join(self.finished_courses)}'

    def __eq__(self, other):
        return medium_grade(self.grades) == medium_grade(other.grades)
    def __ne__(self, other):
        return medium_grade(self.grades) != medium_grade(other.grades)
    def __lt__(self, other):
        return medium_grade(self.grades) < medium_grade(other.grades)
    def __gt__(self, other):
        return medium_grade(self.grades) > medium_grade(other.grades)
    def __eq__(self, other):
        return medium_grade(self.grades) == medium_grade(other.grades)
    def __le__(self, other):
        return medium_grade(self.grades) <= medium_grade(other.grades)
    def __ge__(self, other):
        return medium_grade(self.grades) >= medium_grade(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    def __init__(self, name, surname, ):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФмилия: {self.surname}\nСредняя оценка лекции: {medium_grade(self.grades)}'

    def __eq__(self, other):
        return medium_grade(self.grades) == medium_grade(other.grades)
    def __ne__(self, other):
        return medium_grade(self.grades) != medium_grade(other.grades)
    def __lt__(self, other):
        return medium_grade(self.grades) < medium_grade(other.grades)
    def __gt__(self, other):
        return medium_grade(self.grades) > medium_grade(other.grades)
    def __eq__(self, other):
        return medium_grade(self.grades) == medium_grade(other.grades)
    def __le__(self, other):
        return medium_grade(self.grades) <= medium_grade(other.grades)
    def __ge__(self, other):
        return medium_grade(self.grades) >= medium_grade(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФмилия: {self.surname}'

def medium_grade(grades):
    total = 0
    count = 0
    for grade in grades.values():
        total += sum(grade)
        count += len(grade)
    return total / count

first_student = Student('Ruoy', 'Eman', 'men')
first_student.courses_in_progress += ['Python', 'git']

first_reviewer = Reviewer('Some', 'Buddy')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['git']

first_reviewer.rate_hw(first_student, 'Python', 5)
first_reviewer.rate_hw(first_student, 'Python', 6)
first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'git', 8)
first_reviewer.rate_hw(first_student, 'git', 9)

# print(first_student.grades)

first_lecture = Lecture('Brad', 'Pitt')
first_lecture.courses_attached += ['Python', 'git']

# print(first_lecture.courses_attached)

first_student.rate_lec(first_lecture, 'Python', 10)
first_student.rate_lec(first_lecture, 'Python', 9)
first_student.rate_lec(first_lecture, 'Python', 7)
first_student.rate_lec(first_lecture, 'git', 10)
# print(first_lecture.grades)





second_student = Student('Johnny', 'Lochanta', 'men')
second_student.courses_in_progress += ['Python', 'git', 'django']
second_student.finished_courses += ['soft skills']

second_reviewer = Reviewer('Tom', 'Cruise')
second_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['git']
second_reviewer.courses_attached += ['django']

second_reviewer.rate_hw(second_student, 'Python', 5)
second_reviewer.rate_hw(second_student, 'Python', 6)
second_reviewer.rate_hw(second_student, 'Python', 7)
second_reviewer.rate_hw(second_student, 'git', 8)
second_reviewer.rate_hw(second_student, 'git', 9)
second_reviewer.rate_hw(second_student, 'git', 10)

# print(second_student.grades)

second_lecture = Lecture('Antony', 'Stark')
second_lecture.courses_attached += ['Python', 'git', 'django']

print(second_lecture.courses_attached)

second_student.rate_lec(second_lecture, 'Python', 7)
second_student.rate_lec(second_lecture, 'Python', 6)
second_student.rate_lec(second_lecture, 'Python', 8)
second_student.rate_lec(second_lecture, 'git', 9)
second_student.rate_lec(second_lecture, 'django', 7)
second_student.rate_lec(second_lecture, 'django', 9)
first_student.rate_lec(second_lecture, 'Python', 8)
first_student.rate_lec(second_lecture, 'Python', 9)
first_student.rate_lec(second_lecture, 'Python', 8)
first_student.rate_lec(second_lecture, 'git', 7)
print(second_lecture.grades)

print(first_reviewer, '\n')
print(first_lecture, '\n')
print(first_student, '\n', '\n')

print(second_reviewer, '\n')
print(second_lecture, '\n')
print(second_student, '\n', '\n')

print(first_student >= second_student)
print(first_lecture >= second_lecture)