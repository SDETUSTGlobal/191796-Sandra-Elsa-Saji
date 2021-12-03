from collections import Counter
list1 = ['x','y','z','x','x','x','y', 'z']
print(Counter(list1))
print("________________________________________________")
#Counter with String
from collections import Counter
my_str = "Welcome to Guru99 Tutorials!"
print(Counter(my_str))
print("____________________________________________")
#Counter with List
from collections import Counter
list1 = ['x','y','z','x','x','x','y','z']
print(Counter(list1))
print("________________________________________________")
#Counter with Dictionary
from collections import Counter
dict1 =  {'x': 4, 'y': 2, 'z': 2, 'z': 2}
print(Counter(dict1))
print("________________________________________________")
#Counter with Tuple
from collections import Counter
tuple1 = ('x','y','z','x','x','x','y','z')
print(Counter(tuple1))
print("________________________________________________")
#Initializing Counter
from collections import Counter
print(Counter("Welcome to Python"))  # using string
print(Counter(['x', 'y', 'z', 'x', 'x', 'x', 'y', 'z']))  # using list
print(Counter({'x': 4, 'y': 2, 'z': 2}))  # using dictionary
print(Counter(('x', 'y', 'z', 'x', 'x', 'x', 'y', 'z')))  # using tuple

#Initialize a empty Counter
from collections import Counter
_count = Counter()
#Updating Counter
_count.update('Welcome to Python')

#example:
from collections import Counter
_count = Counter()
_count.update('Welcome to Python')
print(_count)
print("________________________________________________")
#Accessing Counter
from collections import Counter
_count = Counter()
_count.update('Welcome to Guru99 Tutorials!')
print('%s : %d' % ('u', _count['u']))
print('\n')
for char in 'Guru':
    print('%s : %d' % (char, _count[char]))
print("________________________________________________")
#Deleting an Element from Counter
from collections import Counter
dict1 = {'x': 4, 'y': 2, 'z': 2}
del dict1["x"]
print(Counter(dict1))
print("________________________________________________")
#Arithmetic operation on Python Counter
from collections import Counter
counter1 = Counter({'x': 4, 'y': 2, 'z': -2})
counter2 = Counter({'x1': -12, 'y': 5, 'z': 4})
# Addition
counter3 = counter1 + counter2  # only the values that are positive will be returned.
print(counter3)
# Subtraction
counter4 = counter1 - counter2  # all -ve numbers are excluded.For example z will be z = -2-4=-6, since it is -ve value it is not shown in the output
print(counter4)
# Intersection
counter5 = counter1 & counter2  # it will give all common positive minimum values from counter1 and counter2
print(counter5)
# Union
counter6 = counter1 | counter2  # it will give positive max values from counter1 and counter2
print(counter6)
print("________________________________________________")
#Example: elements()
from collections import Counter
counter1 = Counter({'x': 5, 'y': 2, 'z': -2, 'x1': 0})
_elements = counter1.elements()  # will give you all elements with positive value and count>0
for a in _elements:
    print(a)
print("________________________________________________")
#Example: most_common(value)
from collections import Counter
counter1 = Counter({'x': 5, 'y': 12, 'z': -2, 'x1': 0})
common_element = counter1.most_common(2)  # The dictionary will be sorted as per the most common element first followed by next.
print(common_element)
common_element1 = counter1.most_common()  # if the value is not given to most_common , it will sort the dictionary and give the most common elements from the start.The last element will be the least common element.
print(common_element1)
print("________________________________________________")
#Example: subtract()
from collections import Counter
counter1 = Counter({'x': 5, 'y': 12, 'z': -2, 'x1': 0})
counter2 = Counter({'x': 2, 'y': 5})
counter1.subtract(counter2)
print(counter1)
print("________________________________________________")
#Example: update()
from collections import Counter
counter1 = Counter({'x': 5, 'y': 12, 'z': -2, 'x1': 0})
counter2 = Counter({'x': 2, 'y': 5})
counter1.update(counter2)
print(counter1)
print("________________________________________________")
#You can change the count of the element as shown below:
from collections import Counter
counter1 = Counter({'x': 5, 'y': 12, 'z': -2, 'x1': 0})
counter1['y'] = 20
print(counter1)
print("________________________________________________")
#Get and set the count of  Elements using Counter To get the count of an element using Counter you can do as follows:
from collections import Counter
counter1 = Counter({'x': 5, 'y': 12, 'z': -2, 'x1': 0})
print(counter1['y'])  # this will give you the count of element 'y'
#To set the count of the element you can do as follows:
from collections import Counter
counter1 = Counter({'x': 5, 'y': 12, 'z': -2, 'x1': 0})
print(counter1['y'])
counter1['y'] = 20
counter1['y1'] = 10
print(counter1)
print("________________________________________________")