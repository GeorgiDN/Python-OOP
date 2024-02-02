from project import Person
from project import Employee
from project import Teacher

person = Person()
print(person.sleep())

employee = Employee()
print(employee.get_fired())

teacher = Teacher()
print(teacher.teach())

print()
print("Teacher - inherited methods:")
print(teacher.get_fired())  
print(teacher.sleep())  
