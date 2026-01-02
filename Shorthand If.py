a=330
b=330
print("A") if a>b else print("=") if a==b else print("B")

a=10
b=20
bigger= a  if a>b else b
print("bigget is ", bigger)

x=15
y=20
max_value=x if x>y else y
print("max value is ", max_value)

username=""
display_name=username if  username else "Guest"
print("Welcome,", display_name)
