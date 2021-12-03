#Enumerate() in Python Example
mylist = ['A', 'B', 'C', 'D']
e_list = enumerate(mylist)
print(list(e_list))
print("___________________________________________________________")
#UsingEnumerate() on a list with startIndex
mylist = ['A', 'B', 'C', 'D']
e_list = enumerate(mylist, 2)
print(list(e_list))
print("___________________________________________________________")
#Looping Over an Enumerate object
mylist = ['A', 'B', 'C', 'D']
for i in enumerate(mylist):
    print(i)
    print("\n")
print("Using startIndex as 10")
for i in enumerate(mylist, 10):
    print(i)
    print("\n")
print("___________________________________________________________")
#Enumerating a Tuple
my_tuple = ("A", "B", "C", "D", "E")
for i in enumerate(my_tuple):
    print(i)
print("___________________________________________________________")
#Enumerating a String
my_str = "Guru99 "
for i in enumerate(my_str):
    print(i)
print("___________________________________________________________")
#Enumerate a dictionary
my_dict = {"a": "PHP", "b": "JAVA", "c": "PYTHON", "d": "NODEJS"}
for i in enumerate(my_dict):
    print(i)
