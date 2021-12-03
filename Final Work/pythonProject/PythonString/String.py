#accessing values in string
var1 = "Python!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])
print("_____________________________")
#replace
oldstring = 'I like Python'
newstring = oldstring.replace('like', 'love')
print(newstring)
print("_____________________________")
#uppercase lowercase
string="python at Python"
print(string.upper())
# capitalize
string="python at Python"
print(string.capitalize())
#lower
string="PYTHON AT Python"
print(string.lower())
print("_____________________________")
#“join” function
print(":".join("Python"))
print("_____________________________")
#Reversing string
string="12345"
print(''.join(reversed(string)))
print("_____________________________")
#Split Strings
word="Python career Python"
print(word.split(' '))
print("_____________________________")
#strip() Method in Python
str1 = "Welcome to Python!"
after_strip = str1.strip()
#strip() on Invalid Data Type
mylist = ["a", "b", "c", "d"]
#print(mylist.strip())
#strip() Without character parameter
str1 = "Welcome to Python!"
after_strip = str1.strip()
print(after_strip)
str2 = "Welcome to Python!"
after_strip1 = str2.strip()
print(after_strip1)
#strip() Passing character parameters
str1 = "****1Welcome to Python!****"
after_strip = str1.strip("*")
print(after_strip)
str2 = "2Welcome to Python99!"
after_strip1 = str2.strip("99")
print(after_strip1)
str3 = "3Welcome to Python!"
after_strip3 = str3.strip("to")
print(after_strip3)
print("_____________________________")
#Count Method on a String
str1 = "Hello World"
str_count1 = str1.count('o')  # counting the character “o” in the givenstring
print("The count of 'o' is", str_count1)
str_count2 = str1.count('o', 0,5)
print("The count of 'o' usingstart/end is", str_count2)
print("_____________________________")
#Count occurrence of a character in a given string
str1 = "Welcome to Python "
str_count1 = str1.count('u')  # counting the character “u” in the given string
print("The count of 'u' is", str_count1)
str_count2 = str1.count('u', 6,15)
print("The count of 'u' usingstart/end is", str_count2)
print("_____________________________")
#Count occurrence of substring in a given string
str1 = "Welcome to Python "
str_count1 = str1.count('to') # counting the substring “to” in the givenstring
print("The count of 'to' is", str_count1)
str_count2 = str1.count('to', 6,15)
print("The count of 'to' usingstart/end is", str_count2)
print("_____________________________")
