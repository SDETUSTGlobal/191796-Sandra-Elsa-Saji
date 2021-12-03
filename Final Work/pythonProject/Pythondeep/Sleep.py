import time
print("Welcome to Python")
time.sleep(5)
print("This message will be printed after a wait of 5 seconds")
print("_________________________________")
import time
print('Code Execution Started')
def display():
    print('Welcome to Python')
    time.sleep(5)
display()
print('Function Execution Delayed')
print("_________________________________")
import time
my_message = "Python"
for i in my_message:
   print(i)
   time.sleep(1)
print("_________________________________")
import asyncio
print('Code Execution Started')
async def display():
    await asyncio.sleep(5)
    print('Welcome to Python')
asyncio.run(display())
print("_________________________________")
from threading import Event
print('Code Execution Started')
def display():
    print('Welcome to Python')
Event().wait(5)
display()
print("_________________________________")
from threading import Timer
print('Code Execution Started')
def display():
    print('Welcome to Python')
t = Timer(5, display)
t.start()