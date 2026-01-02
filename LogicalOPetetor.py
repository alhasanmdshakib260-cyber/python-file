a=200
b=33
c=500
if a>b and c>a:
    print("Both conditions are true")

a=200
b=33
c=500 
if a>b or a>c:
    print("At least one of the conditions is true ")

a=33
b=200
if not a>b:
    print("a is not greater than b")
age=25
is_student=False
has_discount_code=True
if (age<18 or age>65) and not is_student or has_discount_code:

 print("Discount applies!") 

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

temperature=25
is_raining=False
is_weekend=True

if(temperature>20 and not is_raining) or is_weekend:
   print("great day for outdoor activities!")

username="Tobias"
password="secret12345"
is_verified=True
if username and password and is_verified:
   print("Login successfull!")
else:
   print("login failed")

score=85
if score>=0 and score<=100:
   print("valid score")
else:
   print("invalid score")
   
   


