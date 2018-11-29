def findMinAndMax(L):
    if L==[]:
        return (None, None)
    else:
        max1=L[0]
        min1=L[0]
        for i in L:
            if i>=max1:
                max1=i
            elif i<=min1:
                min1=i
    return (min1,max1)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
