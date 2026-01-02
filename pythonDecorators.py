def changecase(func):
    def myinner():
        return func().upper()
    return myinner
@changecase
def myfunction():
    return"Hello Sally"

@changecase
def otherfunction():
    return "i am speed!"

print(myfunction())
print(otherfunction())


def changecase(func):
     def myinner(x):
         return(x).upper()
     return myinner
@ changecase
def myfunction(nam):
    return "Hello"+ nam
print(myfunction("john"))

def changecase(func):
 def myinner(*args,**kwargs):
     return func(**args,**kwargs)

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))


def changecase(n):
    def changecase(func):
        def myinner():
            if n==1:
                 a==func().upper()
            else:
                 a =func().upper
                 return a
            return myinner
        return changecase
@changecase(1)
def myfunction():
    return "hello linus"
print(myfunction())


def changecase(func):
    def myinner():
        return func().upper()
    return myinner
def addgreeting(func):
    def myinner():
      return "Hello"+func()+"Have a  good day!"
    return myinner
@changecase
@addgreeting
def myffunction():
    return "Tobias"
print(myfunction())  

def myfunction():
    return "Have a great day!"
print(myfunction._name_)


def changecase(func):
    def myinner():
        return "have a great day!"
print(myfunction._name_)


import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name_)




