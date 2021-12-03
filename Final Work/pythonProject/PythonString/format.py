#Empty Placeholder replaced with a string value
print ("Welcome to {} tutorials".format("Python"))
#Empty Placeholder replaced with a numeric value
print ("Welcome to Python{} Tutorials".format("!"))
#Using variable or keyword arguments inside the Placeholder
print ("Welcome to {name}{num} Tutorials".format(name="Python", num="!"))
#Using index or positional arguments inside the Placeholder
print ("Welcome to {0}{1} Tutorials".format("Python","!"))
#Using multiple placeholders inside a string
print ("{} is {} new kind of {} experience!".format("Python", "totally","learning"))
print("_____________________________")
#Using class with format()
class MyClass:
    msg1="Python"
    msg2="Tutorials"
print("Welcome to {c.msg1}! {c.msg2}!".format(c=MyClass()))
print("_____________________________")
#Using dictionary with format()
my_dict = {'msg1': "Welcome", 'msg2': 'Python'}
print("{m[msg1]} to {m[msg2]} Tutorials!".format(m=my_dict))
print("_____________________________")
#Padding Variable Substitutions
print("I have {:5} dogs and {:5} cat".format(2,1))
print("_____________________________")