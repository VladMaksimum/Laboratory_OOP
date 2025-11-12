from House import House
from Student import Student


university = House("Kaliningrad", "Hevskogo", 14)
university.city = "Syzran'"
print(f'Now city = {university.city}')

university.street = "Novaya"
print(f'Now street = {university.street}')

university.number = 10
print(f'Now number = {university.number}')

student = Student("vladislav", "PM", 3)

student.name = "Valentin"
print(f'Now name = {student.name}')

student.profile = "IB"
print(f'Now profile = {student.profile}')

student.labs = 4
print(f'Now labs = {student.labs}')