import math
triangle = [1]

while True:
    temp = 0
    for a in range(1, len(triangle) + 1):
        temp += a 
    triangle.append(temp)
    divisorsCount = 1
    for a in range(2, int(math.sqrt(triangle[-1])) + 1):
        if triangle[-1] % a == 0:
            divisorsCount += 1
    if divisorsCount > 500:
        break

print(triangle[-1])
