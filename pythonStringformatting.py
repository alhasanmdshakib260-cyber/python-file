txt=f"the price is 49 dollers"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt=f"the price is{95:2F}dollers"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price=49
txt=f"It is vary {'Expensive 'if price>50 else 'cheap'}"
print(txt)


fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
    return x*0.3048
txt=f"The plane is flying at a {myconverter(30000)}mater altutude"
print(txt)


price=590000
txt=f"the price is {price:,}dollars"
print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

txt = f"We have {49:8} chickens."
print(txt)

txt = f"The binary version of 5 is {5:%}"

print(txt)

price=49
txt="the price is{}dollars"
price(txt.format(price))

quantity=3
itemno=49
price=49
myorder="I want {}pieces of item number{}for {:.2f}dollars" 
print(myorder.format(quantity,itemno,price))

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
