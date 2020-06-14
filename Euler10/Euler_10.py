import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if (num % i == 0):
            return False
    return True
 
sum = 0
for i in range(2,2000000):
    if isPrime(i):
        sum += i
print(sum)
