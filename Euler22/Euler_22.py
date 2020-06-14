letterToNum = {
    'A': 1,
    'B': 2,
    'C': 3, 
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8, 
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26
    }

temp = []
f = open('names.txt', 'r')
line = f.readline()
temp.append(line.split(','))
words = []
for a in temp[0]:
    a = a[1:-1]
    words.append(a)
sum = 0
tempsum = 0
position = 1
words.sort()
for a in words:
    tempsum = 0
    for b in a:
        tempsum += letterToNum[b]
    sum += tempsum * position
    position += 1
print(sum)
