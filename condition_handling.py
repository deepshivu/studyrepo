import sys
import os
type=sys.argv[1]
if type == "t2.micro":
    print("5 dollars : "+type)
elif type == "t2.medium":
    print("10 dollars : "+type)
else:
    print("invalid input : "+type)
print("password is"+ os.getenv("password"))