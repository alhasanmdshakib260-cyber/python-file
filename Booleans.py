print(10>9)
print(10==9)
print(10<9)

a=200
b=33
if b>a:
    print("b is greatewr than a")
else:
    print("b is not greater than a")

x="hello"
y=15
print(bool(x))
print(bool(y))

bool("abc")
bool(123)
bool(["apple","cherry","banana"])

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
 def __len__(self):
    return 0

myobj=myclass()
print(bool(myobj))


def myFunction():
   return True
print(myFunction())
   

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")   
x=200
print(isinstance(x, int))