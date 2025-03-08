#arithmatic operators + - * / %
a=40
b=20
add=a+b
diff=a-b
mod=a%b
mul=a*b
div=a/b
print("add"+str(add))
print("diff"+str(diff))
print("mod"+str(mod))
print("mul"+str(mul))
print("div"+str(div))

#comparison operators > < >= <= == !=
print("a is greater than b"+str(a>b))
print("a is less than b"+str(a<b))
print("a is greater than or equal to b"+str(a>=b))
print("a is less than or equal to b"+str(a<=b))
print("a is equal to b"+str(a==b))
print("a is not equal to b"+str(a!=b))

#assignment operator = += -= *= /=
c=5
print("c is currently"+str(c))
c+=5
print("c is now"+str(c))
c-=2
print("c is now"+str(c))
c*=2
print("c is now"+str(c))
c/=2
print("c is now"+str(c))

#logical operators and or not
a= True
b=False
print("and of a and bis "+str(a and b))
print("or of a and bis "+str(a or b))
print("or of a and bis "+str(not a))

#identity operators
a=5
b=5
print("a and b are same"+str(a is b))
print("a and b are same"+str(a is not b))