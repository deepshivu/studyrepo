#number=5

def factorial(number):
    result=1
    #range(number) takes i from 0 to number -1
    for i in range(1,number+1):
        result=i*result
    return result
result1=factorial(4)
print(result1)