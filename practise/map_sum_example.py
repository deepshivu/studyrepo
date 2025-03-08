import sys 

nos_list = input("Enter list of numbers separated by spaces: ").split()
sum1 = sum(map(float, nos_list))  # Convert and sum in one line

print("Sum is:", sum1)