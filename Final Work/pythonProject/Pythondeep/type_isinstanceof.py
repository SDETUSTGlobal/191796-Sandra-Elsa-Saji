#Example of type()
str_list = "Welcome to Guru99"
age = 50
pi = 3.14
c_num = 3j+10
my_list = ["A", "B", "C", "D"]
my_tuple = ("A", "B", "C", "D")
my_dict = {"A":"a", "B":"b", "C":"c", "D":"d"}
my_set = {'A', 'B', 'C', 'D'}

print("The type is : ",type(str_list))
print("The type is : ",type(age))
print("The type is : ",type(pi))
print("The type is : ",type(c_num))
print("The type is : ",type(my_list))
print("The type is : ",type(my_tuple))
print("The type is : ",type(my_dict))
print("The type is : ",type(my_set))
print("_______________________________")
#Example: Using type() for class object.
class test:
    s = 'testing'
t = test()
print(type(t))
print("_______________________________")
#Example: Using the name, bases, and dict in type()
class MyClass:
  x = 'Hello World'
  y = 50
t1 = type('NewClass', (MyClass,), dict(x='Hello World', y=50))
print(type(t1))
print(vars(t1))
print("_______________________________")
#Examples of isinstance()
age = isinstance(51,int)
print("age is an integer:", age)
print("_______________________________")
#Example : isinstance() Float check
pi = isinstance(3.14,float)
print("pi is a float:", pi)
print("_______________________________")
#Example: isinstance() String check
message = isinstance("Hello World",str)
print("message is a string:", message)
print("_______________________________")
#Example : isinstance() Tuple check
my_tuple = isinstance((1,2,3,4,5),tuple)
print("my_tuple is a tuple:", my_tuple)
print("_______________________________")
#Example : isinstance() Set check
my_set = isinstance({1,2,3,4,5},set)
print("my_set is a set:", my_set)
print("_______________________________")
#Example: isinstance() list check
my_list = isinstance([1,2,3,4,5],list)
print("my_list is a list:", my_list)
print("_______________________________")
#Example: isinstance() dict check
my_dict = isinstance({"A":"a", "B":"b", "C":"c", "D":"d"},dict)
print("my_dict is a dict:", my_dict)
print("_______________________________")
#Example: isinstance() test on a class
class MyClass:
    _message = "Hello World"
_class = MyClass()
print("_class is a instance of MyClass() : ", isinstance(_class,MyClass))

