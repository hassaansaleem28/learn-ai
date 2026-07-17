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

# -----------------------------------------------------------------------

# jewels = "aA"
# stones = "aAAbbbb"


# def numJewelsInStones():
#     count = 0
#     for i in range(len(stones)):
#         for j in range(len(jewels)):
#             if (jewels[j] == stones[i]):
#                 count += 1
#                 break
#     print(count)


# numJewelsInStones()

# -----------------------------------------------------------------------

# nums = [1, 2, 3, 1]


# def containsDuplicate():
#     seen = set()
#     for i in nums:
#         if i in seen:
#             return True
#         seen.add(i)
#     return False


# print(containsDuplicate())


# --------------------------------------------------------------------------


# s = ["h", "e", "l", "l", "o"]
# left = 0
# right = len(s) - 1
# temp = ""
# while (left <= right):
#     temp = s[left]
#     s[left] = s[right]
#     s[right] = temp
#     left += 1
#     right -= 1

# print(s)


# --------------------------------------------------------------------------


# word1 = "abcd"
# word2 = "pq"

# ans = ""

# for i in range(len(word2) if len(word1) > len(word2) else len(word1)):
#     ans += word1[i]
#     ans += word2[i]

# if (len(word1) > len(word2)):
#     ans += word1[len(word2):]
# if (len(word1) < len(word2)):
#     ans += word2[len(word1):]


# print(ans)


# ----------------------------------------------------------------------------

# n = 15
# ans = [0] * n
# for i in range(0, n):
#     ans[i] = i + 1

# for i in range(0, n):
#     if (ans[i] % 3 == 0 and ans[i] % 5 == 0):
#         ans[i] = "FizzBuzz"
#     elif (ans[i] % 3 == 0):
#         ans[i] = "Fuzz"
#     elif (ans[i] % 5 == 0):
#         ans[i] = "Buzz"
#     else:
#         ans[i] = f"{i + 1}"

# print(ans)


# -------------------------------------------------------------------------------------

# s = "icecream"
# t = "acecreim"


# def isAnagram():
#     if (len(s) != len(t)):
#         print(False)
#     arr = [0] * 26

#     for i in range(len(s)):
#         arr[ord(s[i]) - ord("a")] += 1
#         arr[ord(t[i]) - ord("a")] -= 1

#     for i in arr:
#         if (i != 0):
#             print(False)

#     print(True)


# isAnagram()

# -------------------------------------------------------------------------------------

# s = "A man, a plan, a canal: Panama"


# def isPalindrome(s):
#     def toLower(c):
#         if 'A' <= c <= 'Z':
#             return chr(ord(c) + 32)
#         return c

#     def isAlNum(c):
#         return ('a' <= c <= 'z' or
#                 'A' <= c <= 'Z' or
#                 '0' <= c <= '9')

#     left = 0
#     right = len(s) - 1

#     while (left < right):
#         if (isAlNum(s[left]) and isAlNum(s[right])):
#             if (toLower(s[left]) != toLower(s[right])):
#                 return False
#             left += 1
#             right -= 1
#         if (not isAlNum(s[left])):
#             left += 1
#         if (not isAlNum(s[right])):
#             right -= 1
#     return True


# print(isPalindrome(s))


# -----------------------------------------------------------------------------

# s = "f11"
# t = "b23"


# def isIsomorphic():
#     s_to_t = {}
#     t_to_s = {}

#     for (c1, c2) in zip(s, t):
#         if c1 in s_to_t:
#             if s_to_t[c1] != c2:
#                 return (False)
#         elif c2 in t_to_s:
#             return (False)
#         else:
#             s_to_t[c1] = c2
#             t_to_s[c2] = c1
#     return (True)


# print(isIsomorphic())

# --------------------------------------------------------------------------------
