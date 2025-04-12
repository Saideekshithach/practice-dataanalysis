import re
x="The rain is spain"
y=re.search("^The.*spain$",x)
if y:
    print("yes the match is correct")
else:
    print("Not matching with the pattern")
x="The rain in spain"
y=re.findall("ai",x)
print(y)
r=re.search("\s",x)
print(r)
z=re.split("\s",x)
print(z)
t=re.sub("\s","$",x)
print(t)
pattern=r"\d+"
text="There are 123 apples"
match=re.search(pattern,text)
if match:
    print("Match found",match.group())
pattern=r"Hello"
text="Hello there are c123 apples and oranges"
match=re.search(pattern,text)
if match:
    print("match found",match.group())
else:
    print("not found")
pattern=r"(\d+)-(\d+)-(\d+)"
text="The event is on 2025-03-26"
match=re.search(pattern,text)
if match:
    print("year:",match.group(1))
    print("month:",match.group(2))
    print("Day:",match.group(3))

email_Pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text="pleasecontact us at example@example.com"
match=re.search(email_Pattern,text)
if match:
    print("Email found:",match.group())
#validate a password
#alidate a url "http://www.google.com/






