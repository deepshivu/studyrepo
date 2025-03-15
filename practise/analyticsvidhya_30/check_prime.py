def check_prime():
    start=1
    end=50
    primes=[]
    for num in range(start,end+1):
        if is_prime(num):
            primes.append(num)
    return primes
def is_prime(num):
    if num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True
primes_list=check_prime()
print(primes_list)





