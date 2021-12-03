f=101
e=200
print(f)
print(e)
def somefunction():
    global f
    print(f)
    f ="changing global variable"
somefunction()
print(f)
del e
print(e)

