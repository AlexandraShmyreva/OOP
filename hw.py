class Student:
  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}

  def rate_lecture(self, lecturer, course, grade):
    if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
      if course in lecturer.grades:
        lecturer.grades[course] += [grade]
      else:
        lecturer.grades[course] = [grade]
    else:
      return 'Ошибка'

  def avarage_grade_hw(self):
    for key, value in self.grades.items():
      return(round(sum(value) / len(value), 2))

  def __str__(self):
    return (f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.avarage_grade_hw()} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: {", ".join(self.finished_courses)}')

  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Не является студентом!')
      return
    return self.avarage_grade_hw() < other.avarage_grade_hw()


class Mentor:
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []


class Lecturer(Mentor):
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.grades = {}
    
  def avarage_grade_for_lectures(self):
    for key, value in self.grades.items():
      return(round(sum(value) / len(value), 2))
      
  def __str__(self):
    res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avarage_grade_for_lectures()}'
    return res
    
  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Не является лектором!')
      return
    return self.avarage_grade_for_lectures() < other.avarage_grade_for_lectures()


class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
          student.grades[course] += [grade]
      else:
          student.grades[course] = [grade]
    else:
        return 'Ошибка'

  def __str__(self):
    res = f'Имя: {self.name} \nФамилия: {self.surname}'
    return res


some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']

some_reviewer1 = Reviewer('Alex', 'Lovaly')
some_reviewer1.courses_attached += ['Python']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python']

some_lecturer1 = Lecturer('Some1', 'Buddy1')
some_lecturer1.courses_attached += ['Python']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student1 = Student('Ivan', 'Pupkin', 'your_gender')
some_student1.courses_in_progress += ['Python']
some_student1.courses_in_progress += ['Git']
some_student1.finished_courses += ['Введение в программирование']

some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 8)

some_reviewer.rate_hw(some_student1, 'Python', 9)
some_reviewer.rate_hw(some_student1, 'Python', 5)
some_reviewer.rate_hw(some_student1, 'Python', 8)

some_student.rate_lecture(some_lecturer, 'Python', 8)
some_student.rate_lecture(some_lecturer, 'Python', 7)
some_student.rate_lecture(some_lecturer, 'Python', 7)

some_student1.rate_lecture(some_lecturer1, 'Python', 5)
some_student1.rate_lecture(some_lecturer1, 'Python', 5)
some_student1.rate_lecture(some_lecturer1, 'Python', 5)

print(some_reviewer)
print()
print(some_lecturer)
print()
print(some_student)
print()
print(some_student < some_student1)
print()
print(some_lecturer > some_lecturer1)
print()

student_list = [some_student, some_student1]
def avarage_grade_student(student_list, course_name):
  grades = []
  for student in student_list:
    if isinstance(student, Student):
        if course_name in student.grades:
          grades += student.grades[course_name]
          res = round(sum(grades) / len(grades), 2)
  return res

print(f'Средняя оценка всех студентов по курсу {"Python"}: {avarage_grade_student(student_list, "Python")}')

lecturer_list = [some_lecturer, some_lecturer1]
def avarage_grade_lectures(lecturer_list, course_name):
  grades2 = []
  for lector in lecturer_list:
    if isinstance(lector, Lecturer):
        if course_name in lector.grades:
          grades2 += lector.grades[course_name]
          res = round(sum(grades2) / len(grades2), 2)
  return res

print(f'Средняя оценка всех лекторов по курсу {"Python"}: {avarage_grade_lectures(lecturer_list, "Python")}')