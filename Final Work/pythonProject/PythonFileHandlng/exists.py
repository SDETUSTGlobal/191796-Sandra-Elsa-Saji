import os.path
from os import path
def main():

   print ("File exists:"+str(path.exists('Python.txt')))
   print ("File exists:" + str(path.exists('career.Python.txt')))
   print ("directory exists:" + str(path.exists('myDirectory')))

if __name__== "__main__":
   main()
print("_______________________________________")
import os.path
from os import path
def main():
   print("Is it File?" + str(path.isfile('Python.txt')))
   print("Is it File?" + str(path.isfile('myDirectory')))
if __name__ == "__main__":
   main()
import os.path
from os import path
def main():
   print("Is it Directory?" + str(path.isdir('Python.txt')))
   print("Is it Directory?" + str(path.isdir('myDirectory')))
if __name__ == "__main__":
   main()
print("_______________________________________")
import pathlib
file = pathlib.Path("Python.txt")
if file.exists ():
    print ("File exist")
else:
    print ("File not exist")
