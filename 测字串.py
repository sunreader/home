L1 = ['Hello', 'World', 18, 'ApplE', None]
L2=[]
for ch in L1:
    if isinstance(ch, str):
        L2.append(ch.lower())
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
