#Finds all abundant numbers below 28123
def abundantNumbers():
    arr = []
    for a in range(12, 28123):
        sum = 0
        for b in range(1, int(a/2)+1):
            if a % b == 0:
                sum += b
        if sum > a:
            arr.append(a)
    return arr

arr = abundantNumbers()

#Makes an array that has the sum of abundant numbers below 28123 
sumsarr = []
for a in range(0, len(arr)):
    for b in range(a, len(arr)):
        temp = arr[a] + arr[b]
        if temp >= 28123:
            break
        sumsarr.append(temp)
sumsarr.sort()

#Get the sum of all numbers from 1 to 28122
sum = 0
for a in range(1, 28123):
    sum += a

#Takes the sum and subtracts all numbes that can be gotten by adding two abundant numbers while also checking for duplicates
temp = 0
for a in sumsarr:
    if a == temp:
        continue
    temp = a 
    sum -= a

print(sum)
