def sum_list(lis):
    if len(lis)==1:
        return lis[0]
    return lis[0] + sum_list(lis[1:])

print (sum_list([1, 4, 7, 10]))



def getSum(list):
    if len(list)==0:
        return 0
    else:
        return list[0] + getSum(list[1:]) 
print(getSum([2,4,5,6,7]))

