sum1=0
for i in range(1,967):
    if i%2==1:
        sum1=sum1+i
    else:
        sum1=sum1-i
print(sum1)
s = 0
count = 1
while count <=966:
    if count%2 == 0:
        s -= count
    else:
        s += count
    count += 1
print(s)
