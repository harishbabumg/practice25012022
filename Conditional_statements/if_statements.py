# """WAP to check if the given input number is even"""
# #
# # number = int(input("enter a number: "))
# # print(type(number))
# #
# # if number % 2 == 0:
# #     print("number is even")
#
# """Write a program to check if the given character is in lower case are not"""
# # # char = input("enter any character: ")
# # # if "a" <= char <= "z":
# # #     print(f"{char}is lowercase character")
# # char = input("enter any character: ")
# # if char.islower():
# #     print(f"{char} is lowercase character")
#
# """Write a program to check if the given element is present in the collection or not"""
#
# # list__ = ["python", "java", "ruby", "nodejs"]
# # element = "Java"
# #
# # if element in list__:
# #     print("{element} is a member of list__")
#
#  WAP to print greatest of three numbers

a = 12
b = 20
c = 22

if a <= b <= c:
    print(f"{c} is greatest number")
else:
    print()
if b <= c <= a:
    print(f"{a} is greatest number")
else:
    print()
if c <= b <= b:
    print(f"{b} is greatest number")
else:
    print()




#  OR

# num1 = int(input("Enter num1:"))
# num2 = int(input("Enter num2:"))
# num3 = int(input("Enter num3:"))
# print(max("print greatest of "))

# "WAP to check if the entered character is vowel. If the character is an vowel. create a dictionary with
#  key askii of the character as value

# letter  = "a"
# if letter in "AEIOUaeiou":
#     print (dict([( letter, ord(letter))]))
# else:
#     print( f"{letter} is not a vowel")

#  OR

char = "a"
d = {}

if char.lower() in "aeiou":
    # d[char] = ord(char)
    # d.update({char: ord(char)})
    # print(d.setdefault(char, ord(char)))
    # print({char: ord(char)})

