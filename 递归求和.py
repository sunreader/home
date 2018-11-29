def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
m=input('输入数字:')
print('1+2+..',m,'=',sum(eval(m)))
n=1
while True:
    try:
        sum(n)
        n=n+1
    except:
        break
print('默认递归深度限制:',n-1)
