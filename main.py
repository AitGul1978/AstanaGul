from myclass import Person as p
from child import Student as s

john = p('John', 'John')
print(john)
john.change_name('Johnny')
print(john.name)

john_student = s('John', 'John', 123)
print(john_student)
john_student.change_name('Johnny')
print(john.name)
