# 1) Define a Python class Student(). Using  attributes and methods display the info about student.

# class Student:
#     def __init__(self, name, lastname, grade):
#         self.name = name
#         self.lastname = lastname
#         self.grade = grade
#     def student_info(self):
#         print(f"Student name is {self.name} {self.lastname}, his grade is {self.grade}:")
#
# Sam = Student("Sam", "Smith", 5)
# Sam.student_info()


# 2)Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
# Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to calculate the area of
# the rectangle.
# Create a method display() that display the length, width,
# perimeter and area of an object created using an instantiation on rectangle class.

# class Rectangle:
#     def __init__(self, lenght, width):
#         self.lenght = lenght
#         self.width = width
#     def Perimeter(self):
#         perimeter = 2 * (self.width + self.lenght)
#         return perimeter
#     def Area(self):
#         area = self.width * self.lenght
#         return area
#     def Display(self):
#         print(f"The Rectangle lenght is {self.lenght}, width is {self.width} and its Perimetr is {self.Perimeter()}, Area is {self.Area()}")
#
# rectangle1 = Rectangle(10, 20)
# rectangle1.Display()


# 3)Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
#     def __init__(self,a,b,r):
#         self.a = a
#         self.b = b
#         self.r = r
#  - Define a Area() method of the class which calculates the area of the circle.
#  - Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.


# from math import pi
# class Circle:
#     def __init__(self, a, b, r):
#             self.a = a
#             self.b = b
#             self.r = r
#     def Area(self):
#         area = pi * self.r ** 2
#         return area
#     def Perimeter(self):
#         perimeter = 2 * pi * self.r
#         return perimeter
#     def Display(self):
#         print(f"The Area of Circle is {'%.2f' % self.Area()}, and Perimeter is {'%.2f' % self.Perimeter()}:")
# circle1 = Circle(0, 0, 10)
# circle1.Display()



# 4)Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber
# (numeric type), name (name of the account owner as string type), balance.
# Create a constructor with parameters: accountNumber, name, balance.
# Create a Deposit() method which manages the deposit actions.
# Create a Withdrawal() method  which manages withdrawals actions.
# Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
# Create a display() method to display account details.

# class BankAccount:
#     def __init__(self, accountNumber, name, balance):
#         self.accountNumber = accountNumber
#         self.name = name
#         self.balance = balance
#     def Deposit(self):
#         amount = float(input("Enter amount to be deposited: "))
#         self.balance += amount
#         print(f"Amount Deposited {self.balance}")
#     def Withdrawal(self):
#         amount = float(input("Enter amount to be withdrawal: "))
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"You Withdrew {self.balance}")
#         else:
#             print("Insufficient balance")
#     def bankFees(self):
#         self.balance *= 5
#         print(f" Bank fess {self.balance}")
#     def Display(self):
#         print(f"Account holder {self.name}, number {self.accountNumber}, balance {self.balance}")
#         self.Deposit()
#         self.Withdrawal()
#         self.bankFees()
# jack = BankAccount(11254662, "Jack", 12000)
# jack.Display()
