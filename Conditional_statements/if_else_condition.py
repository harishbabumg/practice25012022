"""WAP to check if the given input number is even or not"""

# number = 3
#
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")

"""Write a program to check if the given character is in lower case are not"""

# char = "R"
# #
# if "a" <= char <= "z":
#     print(f"{char} is lowercase")
#
# else:
#     if "A" <= char <= "Z":
#         print(f"{char} is uppercase")
#     else:
#         print(f"{char} is not an alphabet")

###################################################

# char = "R"
#
# if "a" <= char <= "z":
#     print(f"{char} is lowercase")
#
# elif "A" <= char <= "Z":
#     print(f"{char} is uppercase")
#
# else:
#     print(f"{char} is not an alphabet")

#############################################

# iterable = "hai"
#
# if len(iterable) > 0:
#     print("the iterable is not empty")
# else:
#     print("iterable is empty")
# print()  ########################################
# if bool(iterable):
#     print("Iterable is not empty")
# else:
#     print("Iterable is empty")
#
# print()  #########################################
#
# if iterable:
#     print("not empty")
# else:
#     print("empty")
#
# print()  ##################
#
# value = []
# if value:
#     print("It is not a default value")
# else:
#     print("It is a default value")
#
# print() ###############################
#
# wrd = "2"
#
# # if wrd.islower():
# #     print("letter is lower")
#
# if wrd.islower():
#     print(wrd.upper())
#
# # if wrd.isupper():
# #     print("letter is upper")
#
# elif wrd.isupper():
#     print(wrd.lower())
#
# else:
#     print("Element is not an alphabet")
#
#
# char  = "+"
#
# if "a" <= char <= "z":
#     upper_char = char.upper()
#     print(upper_char)
#
# elif "A" <= char <= "Z":
#     lower_char = char.lower()
#     print(lower_char)
#
# else:
#     print("character is not an alphabet")
#
# ##########################
# print()
# print("next line")
#
# chhr = "E"
#
# if "a" <= chhr <= "z":
#     print(chr(ord(chhr) - 32))
#
# elif "A" <= char <= "Z":
#     print(chr(ord(chhr) + 32))
#
# else:
#     print("character is not an alphabet")
#
#
# #Q5#############
#
# sttrings = "spple"
#
# if sttrings[0] in 'aeiouAEIOU':
#     print('vowel')
# else:
#     print('not vowel')
# #
#
#
# # write a program to check f the string is ending with vowel
#
#
# sttrings = "spple"
#
# if sttrings[-1] in 'aeiouAEIOU':
#     print('vowel')
# else:
#     print('not vowel')
#
#
# #####Q6 WAP check string is palindromeor not
#
# string = "MOM"
# a = string.lower()
#
# if string == string[::-1]:
#     print(f"{string} is a palindrome")
# else:
#     print(f"{string} is not a palindrome")
#
# ####q7#############
#
# integrr = 121
# a = str(integrr)
#
# if a == a[::-1]:
#     print(f"{integrr} is a palindrome")
# else:
#     print(f"{integerr} is a palindrome")
#
#
# #  ########Q7#######WAP to check if the iterable has even numberof elements
#
# ite = "12"
#
# if len(ite) % 2 == 0:
#     print("It has even numbers")
# else:
#     print("Not even")
# #######Q8
#
# list_ = [10, 20, 30, 40]
#
# if len(list_) % 2 == 0:
#     print("it iterable has even numbrerd elements")
# else:
#     print("it has odd numberred elements")
#
# #####WAP to check if the first digit in the given number is even or odd
# numbb = 12326359
# str_numbb = str(numbb)
# if int(str_numbb[0]) % 2 == 0:
#     print("numbb is not odd")
# else:
#     print("Number is an odd")

#  #########

x = [10]
y = [20]
z = [30]
print(x.extend(y))
print(x.extend(z))
print(x)
x.sort()
sd= "22"
int(str(sd))
print(sd)
print(type(sd))
