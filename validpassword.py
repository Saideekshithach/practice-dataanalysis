import re
password=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
text="Sai@1234"
match=re.search(password,text)
if match:
    print("valid password")
else:
    print("Invalid password")


