#list example
list_1=["ram","tim",5,3,"ram"]
print("original list 1 is"+str(list_1))
list_1.append("john")
print("now list 1 is"+str(list_1))
list_1.remove("ram")
print("now list 1 is"+str(list_1))
print("length of list if"+str(len(list_1)))
print("type of list is"+str(type(list_1)))
for i in range(len(list_1)):
    print(list_1[i])

#tuple example
tuple_example=(1,2,"ram","john")
print("type of tuple example is"+str(type(tuple_example)))
print("length of tuple example is"+str(len(tuple_example)))


