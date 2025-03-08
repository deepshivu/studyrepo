import sys
input1=int(sys.argv[1])
operation=sys.argv[2]
input3=int(sys.argv[3])
if operation=="sum":
    result=input1+input3
    print(result)
elif operation=="difference":
    result=input1-input3
    print(result)
else:
    print("invalid input")
