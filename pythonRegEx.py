import re
txt="the rain in spain "
x=re.search("the.*spains&",txt)
print(x)


import re

txt = "The rain in Spain"


x = re.findall("[a-m]", txt)
print(x)

import re

txt = "That will be 59 dollars"


x = re.findall("\d", txt)
print(x)

import re

txt = "hello planet"

x = re.findall("he..o", txt)
print(x)

import re

txt = "hello planet"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")



import re

txt = "hello planet"


x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


import re 
txt+"the rain in spain"
x=re.finadall("\AThe",txt)
print(x)
if x:
  print("Yes,there is a match!")
else:
  print("No match")

  
import re

txt = "The rain in Spain"

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)


import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
