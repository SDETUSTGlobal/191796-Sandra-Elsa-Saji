import os
import shutil
from os import path
def main():
    # make a duplicate of an existing file
    if path.exists("Python.txt"):
        # get the path to the file in the current directory
        src = path.realpath("Python.txt");
        # seperate the path from the filter
    head, tail = path.split(src)
    print("path:" + head)
    print("file:" + tail)
    # let's make a backup copy by appending "bak" to the name
    dst = src + ".bak"
    # nowuse the shell to make a copy of the file
    shutil.copy(src, dst)
    # copy over the permissions,modification
    shutil.copystat(src, dst)
if __name__ == "__main__":
    main()
print("___________________________________________")
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    # Get the modification time
    t = time.ctime(path.getmtime("Python.txt.bak"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("Python.txt.bak")))
if __name__ == "__main__":
    main()
print("____________________________________________________")
import os
import shutil
from os import path
def main():
    # make a duplicate of an existing file
    if path.exists("Python.txt"):
        # get the path to the file in the current directory
        src = path.realpath("Python.txt");
    # rename the original file
    os.rename('Python.txt', 'career.Python.txt')
if __name__ == "__main__":
    main()
