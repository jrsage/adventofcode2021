f = open('Input/2_1.txt', 'r')
lines = f.readlines()
d = 0
h = 0
a = 0
idx = len(lines)

clean = [line.replace('\n', '') for line in lines]

for step in clean:
    if step[0] == 'f':
        h += int(step[-1])
        d += int(step[-1])*a
    elif step[0] == 'd':
        a += int(step[-1])
    else:
        a -= int(step[-1])

print (d)
print (h)
print (d*h)
        
