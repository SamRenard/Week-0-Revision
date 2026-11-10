##task1
numbers=[12,5,8,3,10]
print(numbers[0])
print(numbers[-1])
numbers[1]=20
numbers.append(7)
numbers.remove(8)
print(numbers)
print(len(numbers))

##task2
numbers=[4,15,8,23,10,31,6,42,17,50]
big_numbers=[]
odd_numbers=[]
for number in numbers:
    print(number)
    if number%2==0:
        print(number)
    if number>10:
        big_numbers.append(number)
    if number%2!=0:
        odd_numbers.append(number)
print(big_numbers,len(big_numbers))
print(odd_numbers,len(odd_numbers))

##task3
scores=[45,12,78,45,90,23]
scores.insert(2,60)
print(scores)
scores.append(35)
scores.remove(45)
print(scores)
removed_score=scores.pop()
print(scores)
scores.sort()
print(scores)
scores.reverse()
print(scores)
print(scores.count(45))
print(scores.index(60))
print(scores)
print(removed_score)
print(len(scores))

##task4
student = {
    "name": "Murad",
    "age": 21,
    "course": "Python",
    "score": 75
}
print(student["name"])
print(student["age"])
student["score"] = 90
student["city"] = "Baku"
student["is_active"] = True
del student["course"]
removed_age=student.pop("age")
print(student.keys())
print(student.values())
print(student)
print(len(student))

##task5
scores = {
    "Python": 85,
    "SQL": 72,
    "Git": 90,
    "FastAPI": 65,
    "Django": 95
}
total_score = 0
average=0
for key in scores:
    print(key)
for value in scores.values():
    print(value)
    total_score += value
for key,value in scores.items():
    print(f"{key} : {value}")
average = total_score / len(scores)
print("Total:", total_score)
print("Average:", average)
k=scores.get("JavaScript",0)
print(k)
if "Python" in scores:
    print("Name exist")
if "React" not in scores:
    print("Name does not exist")

##task6
students = {
    "student1": {
        "name": "Ali",
        "age": 20,
        "score": 85
    },
    "student2": {
        "name": "Murad",
        "age": 21,
        "score": 92
    },
    "student3": {
        "name": "Samir",
        "age": 19,
        "score": 68
    },
    "student4": {
        "name": "Rashad",
        "age": 22,
        "score": 75
    },
    "student5": {
        "name": "Kamran",
        "age": 20,
        "score": 96
    }
}
total_score = 0
top_students = {}
students["student2"]["score"]=98
for student_id, information in students.items():
    print(information["name"])
    print(information["score"])
    total_score += information["score"]
    if information["score"] > 80:
        print("Top student:", information["name"])
        top_students[student_id] = information
print(total_score)
average_score = total_score / len(students)
print(top_students,average_score)

##task7
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False
def greet(name="Guest"):
    print("Hello " + name)
print(add(10, 5))
print(subtract(20, 8))
print(multiply(6, 7))
print(divide(20, 4))
print(divide(10, 0))

print(is_even(8))
print(is_even(7))

greet()
greet("Savalan")

##task 8
students = [
    {"name": "Ali", "age": 20, "score": 85},
    {"name": "Murad", "age": 21, "score": 95},
    {"name": "Samir", "age": 19, "score": 68},
    {"name": "Rashad", "age": 22, "score": 75},
    {"name": "Kamran", "age": 20, "score": 96}
]
def show_students(students):
    for student in students:
        print(student["name"], student["age"], student["score"])
def calculate_average(students):
    total = 0
    for student in students:
        total += student["score"]
    total /= len(students)
    return total
def get_top_students(students,minimum_score=80):
    top_students = []
    for student in students:
        if student["score"] > minimum_score:
            top_students.append(student)
    return top_students
def find_student(students,name):
    for student in students:
        if student["name"] == name:
            return student
    return None
def count_students(students):
    count = 0
    for student in students:
        count+=1
    return count
show_students(students)

print("Average:", calculate_average(students))

print("Top students:", get_top_students(students))

print("Top students above 90:", get_top_students(students, 90))

print("Find student:", find_student(students, "Murad"))

print("Student count:", count_students(students))

print("Unknown student:", find_student(students, "John"))

##task 9
with open("students.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)
with open("students.txt","r",encoding="utf-8") as file:
    line1=file.readline()
    line2=file.readline()
    print(line1,end="")
    print(line2,end="")
with open("students.txt","r",encoding="utf-8") as file:
    student_names=file.readlines()
print(len(student_names))
for name in student_names:
    print(name.strip())

###task 10

import json


def load_students():
    with open("students.json", "r", encoding="utf-8") as file:
        students = json.load(file)

    return students


def save_students(students):
    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)


def add_student(students, name, age, score):
    new_student = {
        "name": name,
        "age": age,
        "score": score
    }

    students.append(new_student)
    save_students(students)


def show_students(students):
    for student in students:
        print(
            student["name"],
            student["age"],
            student["score"]
        )


def get_top_students(students, minimum_score=80):
    top_students = []

    for student in students:
        if student["score"] > minimum_score:
            top_students.append(student)

    return top_students


# Main program
students = load_students()

add_student(students, "Savalan", 20, 98)

print("\nAll students:")
show_students(students)

print("\nTop students:")
print(get_top_students(students))

print("\nStudents above 90:")
print(get_top_students(students, 90))

##bank_account_class
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
        if balance < 0:
            raise ValueError("Balance cannot be negative")
    def deposit(self,amount):
        if amount<0 or amount==0:
            raise ValueError('amount must be positive')
        self.balance += amount
        return self
    def withdraw(self,amount):
        if amount > self.balance:
            raise ValueError("Not enough money")
        if amount<=0:
            raise ValueError('amount must be positive')
        self.balance -= amount
        return self
    def transfer(self,account,amount):
        if amount==0 or amount<0:
            raise ValueError('amount must be positive')
        if amount > self.balance:
            raise ValueError("Not enough money")
        self.withdraw(amount)
        account.deposit(amount)
    def show_new_balance(self):
        print("New balance:",self.balance)
savalan = BankAccount(500)
ali = BankAccount(200)

savalan.transfer(ali, 100)

savalan.show_new_balance()
ali.show_new_balance()
savalan.transfer(ali, 1000)
