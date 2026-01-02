x="awesome"
def myfunc():
    print("python is"+x)
myfunc() 

print("python is"+x)
x="awesome"
def myfunc():
    global x
    x="fantastic"

myfunc()
print("python is"+x) 

