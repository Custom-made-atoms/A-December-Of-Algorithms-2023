import random as r

num = int(input("Enter a number: "))
arr = [[0 for i in range(num)] for j in range(num)]

sum = int(((num**2+1)/2)*num)

def add(arr,sum):
    count2 = 0
    TorF = 0
    for i in arr:
        count1 = 0
        for j in i:
            count1 += j
        if count1 != sum:
            return False
    for i in range(len(arr)):
        for k in range(len(arr)):
            for j in arr:
                count2 += j[k]
            if count2 != sum:
                return False
            else:
                count2 = 0                
    count3 = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                count3 += arr[i][i]
    if count3 != sum:
        return False
    if TorF == 0:
        return True
    
def mat(arr):
    num_list = [i for i in range(1,num**2 + 1)]
    for i in range(len(arr)):
        for j in range(len(arr)):
            rnum = r.choice(num_list)
            arr[i][j] = rnum
            num_list.remove(rnum)

    if add(arr,sum):
        print('Yes')
        print(arr)
        global con
        con = 0

con = 1
while con == 1:
    mat(arr)

    
    