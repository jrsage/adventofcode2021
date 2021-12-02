f = open('Input/1_1.txt', 'r')
lines = f.readlines()
c = 0
idx = len(lines)

clean = [line.replace('/n', '') for line in lines]

for i in range(3,idx):
    b = int(clean[i])+int(clean[i-1])+int(clean[i-2])
    a = int(clean[i-1])+int(clean[i-2])+int(clean[i-3])
    if b>a: c+=1

print (c)
