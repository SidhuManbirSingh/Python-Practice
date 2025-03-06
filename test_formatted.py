#########################################################
# Section 1: Arithmetic and Basic I/O Operations
#########################################################
# Example: Sum of two numbers and area & perimeter calculation.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# sum = num1 + num2
# print(f"The sum of {num1} and {num2} is {sum}")
#
# a = int(input("Enter the first side: "))
# print(f"Area: {a * a} and Perimeter: {4 * a}")

#########################################################
# Section 2: String Slicing and Manipulation
#########################################################
'''
str = "Hello,World!"
# Slicing examples:
print(str[0:5])          # Prints "Hello"
print(str[6:len(str)])    # Prints "World!"
print(str[1:])           # Prints from index 1 to end
print(str[:5])           # Another way to get "Hello"
print(str[-1:])          # Prints the last character "!"
print(str[::-1])         # Reverses the string
a = 2
print(str[::a])          # Prints every 2nd character
'''

#########################################################
# Section 3: Conditional Statements and Grade Calculation
#########################################################
# Using conditionals to assign a grade based on marks.
# grade = None
# marks = 63
# if marks >= 90:
#     grade = "A"
# elif 80 <= marks < 90:
#     grade = "B"
# elif 70 <= marks < 80:
#     grade = "C"
# elif 60 <= marks < 70:
#     grade = "D"
# elif 50 <= marks < 60:
#     grade = "E"
# else:
#     grade = "F"
# print(f"Grade: {grade}")

#########################################################
# Section 4: Finding the Largest Number Among Three
#########################################################
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))
# if num1 > num2 and num1 > num3:
#     print(f"{num1} is the largest number")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is the largest number")
# else:
#     print(f"{num3} is the largest number")

#########################################################
# Section 5: Modulus Operation Example
#########################################################
# num1 = int(input("Enter the first number: "))
# print(f"{num1 % 7 == 0}")  # Prints True if num1 is divisible by 7, else False

#########################################################
# Section 6: List and String Operations, Palindrome Check
#########################################################
# Taking movie inputs and checking if a word is a palindrome.
# f1 = str(input("Enter the first movie: "))
# f2 = str(input("Enter the second movie: "))
# f3 = str(input("Enter the third movie: "))
# movies = [f1, f2, f3]
# print(movies)
#
# list_str = "madam"
# if list_str == list_str[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

#########################################################
# Section 7: List Sorting and Reversing
#########################################################
# grades = ["A", "B", "A", "C", "A", "B", "A", "C", "B", "A"]
# grades.sort()             # Sorts in ascending order
# copy_grades = grades[::-1]  # Reverses the sorted list
# print(copy_grades)

#########################################################
# Section 8: Set Operations and Duplicate Removal
#########################################################
# set_1 = {1, 2, 2, 3, 4, 5}  # Duplicate values removed automatically
# print(set_1)
#
# set2 = {9.0, 9}  # 9 and 9.0 are considered equal in a set
# print(set2)
#
# set2 = {9.0, 9, '10.0', 10}  # Mix of numbers and string
# print(set_1)
# print(set2)

#########################################################
# Section 9: Looping Constructs (for and while loops)
#########################################################
# For-loop over a list
# cal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for val in cal:
#     print(val)
#
# While-loop counting from 1 to 100
# count = 1
# while count != 101:
#     print(count)
#     count += 1
#
# While-loop counting down from 100 to 1
# count = 100
# while count != 0:
#     print(count)
#     count -= 1
#
# Multiplication table for number 21 (first 10 multiples)
# z = 21
# n = 1
# while n != 11:
#     print(f"{z} X {n} = {z * n}")
#     n += 1
#
# Simple for-loop with range
# for e in range(1, 101):
#     print(e)

#########################################################
# Section 10: Summation and Factorial Calculations
#########################################################
# Summation logic using a while loop
# n = 5
# x = 0
# total = 0
# while x <= n:
#     total += x
#     x += 1
# print(total)
#
# Factorial using recursion
# n = 5
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
# print(fact(n))
#
# Factorial using loop iteration
# val = 1
# for el in range(1, n + 1):
#     val *= el
# print(val)

#########################################################
# Section 11: List Utilities and Recursion Examples
#########################################################
# Function to return list length
# def list_length(lst):
#     return len(lst)
# sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_length(sample_list))
#
# Function to print each element in a list
# def print_list(lst):
#     for el in lst:
#         print(el)
# print_list(sample_list)
#
# Simple recursive function (alternative factorial)
# def recurrsion(n):
#     if n == 0:
#         return 1
#     else:
#         return n * recurrsion(n - 1)
# print(recurrsion(5))

#########################################################
# Section 12: Working with External Libraries (Requests)
#########################################################
# import requests
# def get_exchange_rate(foreign_currency):
#     url = "https://api.exchangerate-api.com/v4/latest/" + foreign_currency
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         return data['rates']['INR']
#     else:
#         raise Exception("Error fetching exchange rate data")
#
# try:
#     usd = float(input("Enter the amount in USD: "))
#     rate = get_exchange_rate("USD")
#     print(f"The current INR to USD exchange rate is: {rate}")
# except Exception as e:
#     print(e)

#########################################################
# Section 13: File Operations (Read, Write, Update)
#########################################################
# import os
# os.remove("customer_data.csv")  # Remove a file (be careful!)
#
# Writing to a file with "w+"
# with open("Test.txt", "w+") as file:
#     file.write("Hi everyone, we are learning File I/O using Java.\nI like Java programming.")
#
# Reading a file, modifying its contents, and writing back
# with open("Test.txt", "r") as file:
#     data = file.read()
# new_data = data.replace("Java", "Python")
# with open("Test.txt", "w") as file:
#     file.write(new_data)
#     print("Update complete")
#
# Reading file line-by-line and checking for a word
# with open("Test.txt", "r") as file:
#     count = 1
#     while not file.closed:
#         data = file.readline()
#         if "learning" in data:
#             print(f"The word 'learning' is present in the file at row {count}")
#         else:
#             print(f"The word 'learning' is not present in the file at row {count}")
#         count += 1

#########################################################
# Section 14: Measuring Execution Time (Using time module)
#########################################################
# import time
# start_time = time.time()
# count = 0
# while count != 100001:
#     print(f"row: {count}")
#     count += 1
# end_time = time.time()
# execution_time = end_time - start_time
# print(f"Execution time: {execution_time} seconds")

#########################################################
# Section 15: CSV File Operations
#########################################################
# import csv
# def print_even_numbers_from_csv(file_path):
#     with open(file_path, 'r') as file:  # Open in read mode
#         csv_reader = csv.reader(file)
#         for row in csv_reader:
#             for item in row:
#                 try:
#                     number = int(item)
#                     if number % 2 == 0:
#                         print(number)
#                 except ValueError:
#                     continue
#
# # Example usage for printing even numbers from CSV:
# file_path = 'test.csv'
# print_even_numbers_from_csv(file_path)
#
# Another example: Counting even numbers from a CSV file:
# count = 0 
# with open("Test.csv", "r") as file:
#     data = file.read()
#     nums = data.split(',')
#     for val in nums:
#         if int(val) % 2 == 0:
#             count += 1
#     print(f"Total even numbers: {count}")

#########################################################
# Section 16: Object Oriented Programming (OOP) Examples
#########################################################

# --- Student Average Calculation ---
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def average(self):
#         return sum(self.marks) / len(self.marks)
#
# s = Student("John", [90, 80, 70, 60, 50])
# print(s.average())


# --- Bank Operations Example ---
# class Bank:
#     bank_name = "ABC Bank"
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Amount deposited: {amount}")
#     def withdraw(self, amount):
#         if amount >= self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"Amount withdrawn: {amount}")
#     def getBalance(self):
#         return self.balance
#
# b = Bank("John", 1000)
# print(f"Balance: {b.getBalance()}")
# b.deposit(500)
# b.deposit(500)
# b.deposit(500)
# print(b.bank_name)
# print(f"Balance: {b.getBalance()}")


# --- Object Attribute Manipulation (Person Class) ---
# class Student:
#     def __init__(self, name):
#         self.name = name
#
# s = Student("John")
# print(s.name)
# try:
#     print(s.name)
# except NameError:
#     print("The object 's' no longer exists.")


# --- Encapsulation Example (Account Class) ---
# class Account:
#     def __init__(self, acc_number, acc_pass):
#         self.__acc_number = acc_number
#         self.__acc_pass = acc_pass
#     def to_String(self):
#         return f"Account number: {self.__acc_number} and Password: {self.__acc_pass}"
#
# acc = Account(12345, "password")
# print(acc.to_String())


# --- Inheritance Example: Car Classes ---
# class Car:
#     brand = "Toyota"
#     def __init__(self, type):
#         self.type = type
#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")
#
# class ToyotaCar(Car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#     @classmethod
#     def getBrand(cls):
#         return cls.brand
#     def changeBrand(self, brand):
#         self.__class__.brand = brand
#
# car1 = ToyotaCar("prius", "electric")
# car1.changeBrand("Honda123")
# print(car1.brand)


# --- Inheritance, Overriding and Multiple Inheritance Examples ---
# class Car:
#     @staticmethod
#     def start():
#         return "car started.."
#     @staticmethod
#     def stop():
#         return "car stopped.."
#
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name
#
# class Fortuner(ToyotaCar):
#     def __init__(self, name, type):
#         super().__init__(name)
#         self.type = type
#
# f = Fortuner("Fortuner", "SUV")
# print(f.name)
# print(f.type)
#
# # Multiple Inheritance and MRO Example:
# class A:
#     a = "Welcome A"
#     x = "Welcome A.X"
#
# class B:
#     b = "Welcome B"
#     x = "Welcome B.X"
#
# class C(B, A):
#     c = "Welcome C"
#     x = "Welcome X"
#
# print(C.x)
#
# # Basic Inheritance with Computer and Laptop Classes:
# class Computer:
#     def __init__(self, brand):
#         self.brand = brand
#
# class Laptop(Computer):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model


# --- Property and Attribute Manipulation (Person Class) ---
# class Person:
#     name = "Anonymous"
#     def __init__(self, p, c, m):
#         self.p = p
#         self.c = c
#         self.m = m
#         self.percent = (self.p + self.c + self.m) / 3  # Initialize percent
#     @property
#     def percentage(self):
#         self.percent = (self.p + self.c + self.m) / 3  # Update percent
#         return self.percent
#     def changeName(self, name):
#         self.name = name
#
# p1 = Person(5, 6, 7)
# print(p1.percentage)
# p1.p = 99
# print(p1.percentage)
# print(p1.percent)
# print(p1.percentage)


# --- Improved Student Class (Java-like setter approach) ---
# class Student:
#     def __init__(self, phy, chem, bio):
#         self.phy = phy
#         self.chem = chem
#         self.bio = bio
#         self.set_percentage(self.phy, self.chem, self.bio)
#
#     def set_physics(self, phy):
#         self.phy = phy
#         self.set_percentage(self.phy, self.chem, self.bio)
#
#     def set_percentage(self, phy, chem, bio):
#         self.percent = (self.phy + self.chem + self.bio) / 3
#
#     def get_percentage(self):
#         return self.percent
#
# s = Student(5, 6, 7)
# print(s.get_percentage())
# s.set_physics(9)
# print(s.get_percentage())


# --- Student Class with calcPercentage method ---
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
#     def calcPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
#
# stu1 = Student(98, 97, 99)
# print(stu1.percentage)
# stu1.phy = 86
# print(stu1.phy)
# stu1.calcPercentage()
# print(stu1.percentage)



