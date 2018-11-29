ch=''
for i in range(111,1000):
    a=i//100
    b=(i-a*100)//10
    c=i-100*a-10*b
    if i==a**3+b**3+c**3:
        ch=ch+str(i)+','
print(ch[:-1])
s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
        s += "{},".format(i)
print(s[:-1])
