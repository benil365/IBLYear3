

email =input("what is ypour email address:").strip()
username,domain = email.split("@")

if username and "."in domain:
  print("valid")
  print(email)
else:
   print("invalid email address")


#senior
# This code is checking if the email address entered by the user is valid or not using regular
# expressions. It first imports the `re` module which provides support for regular expressions. Then
# it prompts the user to enter their email address and strips any leading or trailing spaces. It then
# uses the `re.search()` function to search for the "@" symbol in the email address. If it finds the
# "@" symbol, it prints "valid", otherwise it prints "invalid".
import re
email =input("what is ypour email address:").strip()
if re.search(r"\^.+@.+\.com\$",email):
   print("valid")
else:
    print("invalid")