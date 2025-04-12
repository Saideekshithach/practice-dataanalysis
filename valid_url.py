import re
url=r"^https?://www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$"
text="https://www.google.com/"
match=re.search(url,text)
if match:
    print("valid url")
else:
    print("Invalid url")