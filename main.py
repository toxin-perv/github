# class programmer:
#     company = "microsoft"
#     def __init__(self, name, salary, lan):
#         self.name = name
#         self.salary = salary
#         self.lan = lan

# r = programmer("ranjan", 1222, "python")
# print(r.name, r.salary, r.lan)

# p = programmer("pri", 4322, "java")
# print(p.name, p.salary, p.lan, p.company)

# n = int(input("enter the num: "))
# class calculator:
#     def __init__(self, square , cube, squareroot):
#         self.square = n*n
#         self.cube = n**3
#         self.cuberoot = n**(1/2)
#     @staticmethod
#     def __init__():
#         print("heloo there")

# cal = calculator(n, n, n)
# print(f"""the square is {cal.square},the cube is  {cal.cube},the cuberoot is  {cal.cuberoot}""")

# a = calculator.__init__(self,square , cube)
# a.greet
# a.square()
# a.cube()
# a.cuberoot()
# class demo :
#     a = 5

# o = demo()
# o.a = 0
 
# print(o.a)
# print(demo.a)


# import math

# n = int(input("Enter the number: "))

# class Calculator:
#     def __init__(self, n):
#         self.square = n * n
#         self.cube = n ** 3
#         self.squareroot = n**(1/2)
    
#     @staticmethod
#     def greet():
#         print("Hello there")

# # Create an instance of Calculator
# cal = Calculator(n)
# cal.greet()
# # Use instance attributes
# print(f"The square is {cal.square}, the cube is {cal.cube}, the square root is {cal.squareroot}")

# # Call the greet method

# class train:
#     def __init__(ranjan, trainNo):
#        ranjan.train = trainNo
#     def book(self, fro, to):
#         print(f"ticket is booked for train {self.train}, from {fro} to {to}")
#     def status(self):
#         print(f"the train {self.train} is running today")
#     def fair(self, fro, to):
#         print(f"the fair of ticket from {fro} to {to} is Rs.12333")
    
# a = train(1222)

# a.book("mumbai", "kashmir")
# a.status()
# a.fair("mumbai", "kashmir")


# class twodvector:
#     def __init__(self, i, j):
#         self.i = i
#         self.j = j
#     def show(self):
#             print(f"{self.i}i, {self.j}j")
# class threedvector(twodvector):
#     def __init__(self, i, j, k):
#         super().__init__(i, j)
#         self.k = k
#     def show(self):
#             print(f"{self.i}i, {self.j}j, {self.k}k")
# a = twodvector(1, 2)
# a.show()
# b = threedvector(1, 2, 6)
# b.show()



# class pets:
#     pass
# class animals(pets):
#     pass
# class dog(animals):
#     def bark(self):
#         print("bow bow")
# a = dog()
# a.bark()

# class employee():
#     salary = 20000
#     increment = 20

#     @property
#     def salaryafterincremnet(self):
#         print(f"salary after incremnet is {self.salary + (self.increment/100)*self.salary}")


#     @salaryafterincremnet.setter(salaryafterincremnet)
#     def increment(salaryafterincrement):
#         print(f"increment value is {((self.salaryafterincremnet/self.salary)-1)*100}")

# a = employee()

# print(a.salaryafterincremnet())
# print(a.increment())


# s = int(input("salary: "))
# i = int(input("increment: "))

# class Employee:
#     salary = s
#     increment = i

#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + (self.increment / 100) * self.salary

#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self, salaryAfterIncrement):
#         self.increment = ((salaryAfterIncrement / self.salary) - 1) * 100

# # Create an instance of Employee
# a = Employee()

# # Set a new salary after increment
# a.salaryAfterIncrement = a.salary + (a.increment/100)*a.salary

# # Print the updated increment
# print(f"Increment value is {a.increment}")

# # Print the salary after increment
# print(f"Salary after increment is {a.salaryAfterIncrement}")



# class complex:
#     def __init__(self, r, i):
#             self.r = r
#             self.i = i
#     def __add__(self, c):
#           return f"{self.r + c.r} , {self.i + c.i}i"
    
#     def __mul__(self, c):
#         real_part = self.r * c.r - self.i * c.i
#         imag_part = self.r * c.i + self.i * c.r
#         return complex(real_part, imag_part)
#     def __str__(self):
#           return f"{self.r}, {self.i}i"


# a = complex(1, 4)
# b = complex(4, 5)

# print(a + b)
# print(a*b)



# class vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __add__(self, v2):
#         return vector(self.i + v2.i , self.j + v2.j, self.k + v2.k)
    
#     def __mul__(self, v2):
#         return vector(self.i * v2.i, self.j * v2.j, self.k * v2.k)
    
#     def __str__(self):
#         return f"{self.i}i + {self.j}j +  {self.k}k"


# a = vector(1, 2, 3)
# b = vector(2, 3, 4)
# c = vector(5, 6, 7)
# print(f"{a + b} is sum of vector")
# print(f"{a * b} is product of vector")
# print(a + c)
# print(a * c)
# class vector:
#     def __init__(self,7 , 8, 10):
#         self.i = 7
#         self.j = 8
#         self.k = 10

#     def __str__(self):
#         print(f"{self.i}i + {self.j}j + {self.k}k")

# a =  vector()


# class Vector:
#     def __init__(self, l): 
#         self.l = l

    
    
#     def __len__(self):
#         return len(self.l)

# # Test the implementation
# v1 = Vector([1, 2, 3, 5]) 
# print(len(v1))
        
# from random import randint

# n = randint(0, 100)

# o = -1

# a = 1

# while (o != n):
#     o = int(input("guess the number: "))
#     if (o > n):
#         print("lower number please")
        
#     elif(o < n):
#         print("upper number please")
        
#     a += 1
    
# if (n == o):
#     print(f"your guess the right number in {a} attempts")
# try:
#     with (
#         open('come.txt') as f1,
#         open ('with.txt') as f2,
#         open('work.txt') as f3
# ):
#         a = f1.read()
#         b = f2.read()
#         c = f3.read()

#     print(a)
#     print(b)
#     print(c)
# except Exception as e:
#     print("file not avalaible")


# l = [2, 4, 5, 6, 7, 8]

# for i,item in enumerate(l):
#     if i==1 or i==4 or i==3:
#      print(item)
# n = int(input("enter the mun:  "))

# table = [n*i for i in range(1, 21)]

# print(table)

# with open("table.txt", "a") as f:
#     f.write(f"the table of {n} is {str(table)}\n")


# a = int(input("enter the mun a:  "))
        
# b = int(input("enter the mun b:  "))

# try:
#     print(a/b)


# except ZeroDivisionError:
#         # if(b == 0):
#         print("connot divide it")



# name = input("enter the name: ")
# age = int(input("enter the age: "))
# phone = int(input("enter the phone : "))

# a = "the name of student is {} its age is {} and number is {}".format(name, age, phone)
# print(a)


# table =  [str(7*i) for i in range (1, 11)]
# # print(table)
# a = "\n".join( table)
# print(a)

# a  = [1,2,34234,53,6234235,64343, 65,754,45,55]
# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     return False
# f = list(filter(divisible5, a))
# print(f)
# a  = [1,2,34234,53,6234235,64343, 65,754,45,55]

# from functools import reduce
# l  = [111, 2, 65, 5, 635, 65, 74, 45,55]


# def greater(a, b):
#     # if (a>b):
#     #     return a 
#     # return b
#     return a + b
# print(reduce(greater, l))

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# app.run() 


# import pyautogui

# while True:
#     pyautogui.keyDown("r")
#     pyautogui.keyDown("a")
#     pyautogui.keyDown("n")
#     pyautogui.keyDown("j")
#     pyautogui.keyDown("a")
#     pyautogui.keyDown("n")
