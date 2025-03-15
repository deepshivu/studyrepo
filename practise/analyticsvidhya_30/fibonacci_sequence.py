def fibonacci_seq(n):
    fibonacci_sequence=[0,1]
    for i in range(2,n):
        next_term=fibonacci_sequence[-1]+fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence
result=fibonacci_seq(10)
print(result)
def list1():
    list1_nos=[1,2,3,4,5]
    print(list1_nos[-2])
list1()