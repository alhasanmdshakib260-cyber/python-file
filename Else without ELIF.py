a=44
b=33
if a>b:
    print("a is grater than b")
else:
    print("b is grater than a")

number=-10
if number%2==0:
    print("the number is even")
else:
    print("the number is odd")

temperature=22
if temperature>30:
    print("it is a hot day")
elif temperature>20:
    print("It is a warm day")
elif temperature>10:
    print("It is a cold outside")
else:
    print("it is a cold outside") 

username="Emil"
if len(username)>0:
    print(f"Welcome,{username}!")
else:
    print("Error: Username cannot be empty")
