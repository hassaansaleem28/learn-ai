# # print("Hello World!")

# import math
# is_prime = 10
# print(is_prime)

# message = """ Hi, I'm Hassaan
# Hi! mom!
# I'm from lahore Pakistan!
# wow how nice you are!
# you take the 3rd row and give your mom the 10th row?
# how shit son you are!
# how tall are you?
# things that are in my mind that I have to do is:

# 01- Start AI Engineering
# 02- LFX preparation
# 03- Upcoming Hackathon Project
# 04- Portfolio
# 05- Leetcode
# 06- Observability work at OWASP Nest
# 07- Upwork or Fiverr?
# """

# first_name = "Hassaan"
# last_name = "Saleem"

# print(f"{first_name} {last_name}")
# print(len(first_name))
# print(first_name[0:3])
# print(first_name[:3])
# print(first_name[0:-1])

# """"String Methods"""

# print(f"{first_name} {last_name}".lower())
# course = "  python course"
# print(course.title())

# print(course.strip())  # remove the space -> lstrip() + rstrip()

# print(course.find("Cou"))
# print(course.replace("o", "i"))

# print("Cou" in course)
# print("swift" not in course)

# x = 1 + 2j
# print(x)

# print(49/5)
# print(10/3)  # it will give a float

# print(10 // 3)  # want an integer ? use this.

# y = -100.6
# # y += 10
# print(y)

# print(round(y))
# print(abs(y))

# ------------------------------------
# gx = int(input("Enter x: "))
# print(gx + 5)

# full_name = "Ahad Ali"
# uni_name = "University of Education"

# if full_name and uni_name:
#     print("Eligible for scholarship")
# elif full_name or uni_name:
#     print("not eligible")
# else:
#     print("try again!")


# for num in range(1, 10, 2):
#     print("Attempt", num, (num) * "*")


# def check_prime(num):

#     if (num < 2):
#         print("Not Prime")
#         return
#     for i in range(2, (num // 2 + 1)):
#         if (num % i == 0):
#             print("Not Prime")
#             return

#     print("Prime Number")


# check_prime(4)

# Nested loop

# for i in range(5):
#     for j in range(5):
#         print(f"({i}, {j})")

# x = int(input("Enter val: "))
# for num in range(x + 1):
#     print(num * "*")


# num = 100
# while num > 0:
#     print(num)
#     num = num // 2

# command = ""
# while (command != "quit"):
#     command = input(">")
#     print("ECHO", command)

# print("By Hassaan:")
# count = 0

# for num in range(1, 50):
#     if (num % 2 == 0):
#         count += 1
#         print(num)

# print(f"We have {count} even numbers.")

# ---------------------------------------------------------------------------------

# operations = ["--X", "X++", "X++"]

# x = 0
# for i in range(len(operations)):
#     print("Hi")
#     if (operations[i] == 'X++' or operations[i] == '++X'):
#         x += 1
#     if (operations[i] == '--X' or operations[i] == 'X--'):
#         x -= 1

# print(x)

# nums = [-4, -1, 0, 3, 10]

# # ---------------------------------------------------------------------------------


# def sortedSquares():
#     for i in range(len(nums)):
#         nums[i] = nums[i] * nums[i]
#     nums.sort()
#     print(nums)


# sortedSquares()

# # ---------------------------------------------------------------------------------

# nums = [1, 2, 3]


# def getConcatenation():
#     n = len(nums)
#     arr = [0] * (n*2)
#     for i in range(len(nums)):
#         arr[i] = nums[i]
#         arr[i+n] = nums[i]
#     print(arr)


# getConcatenation()

# # # ---------------------------------------------------------------------------------

# nums = [1, 1, 1, 1]


# def numIdenticalPairs():
#     count = 0
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if (nums[i] == nums[j] and i < j):
#                 count += 1
#     print(count)


# numIdenticalPairs()

# # # ---------------------------------------------------------------------------------

# nums = [2, 3, 4, 5, 6, 7]
# n = 3


# def shuffle():
#     arr = [0] * len(nums)
#     for i in range(0, len(nums), 2):
#         arr[i] = nums[i // 2]
#         arr[i+1] = nums[n + i // 2]
#     print(arr)


# shuffle()

# ---------------------------------------------------------------------------------

# nums = [0, 1, 0, 3, 12]


# def moveZeroes():
#     point = 0
#     for i in range(len(nums)):
#         if (nums[i] != 0):
#             nums[point] = nums[i]
#             if (i != point):
#                 nums[i] = 0
#             point += 1
#     print(nums)


# moveZeroes()


# ---------------------------------------------------------------------------------
# nums = [1, 1, 0, 1, 1, 1]


# def findMaxConsecutiveOnes():
#     numofOnes = 0
#     maxVal = 0

#     for i in range(len(nums)):
#         if (nums[i] == 1):
#             numofOnes += 1
#             maxVal = max(numofOnes, maxVal)
#         else:
#             numofOnes = 0
#     print(maxVal)


# findMaxConsecutiveOnes()

# # ---------------------------------------------------------------------------------

# nums = [1, 2, 3, 4, 5, 6, 7]s


# def rotate(k):
#     k = k % len(nums)
#     nums.reverse()
#     nums[:k] = nums[:k][::-1]
#     nums[k:] = nums[k:][::-1]
#     print(nums)


# rotate(3)
