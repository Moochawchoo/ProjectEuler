def divisorCount(b):
    divisors = 0
    for a in range(1, int(b/2)+1):
        if b % a == 0:
            divisors += a
    return divisors

sum = 0
for a in range(1, 10000):
    b = divisorCount(a)
    if a == divisorCount(b) and a != b:
        sum += a
print(sum)
