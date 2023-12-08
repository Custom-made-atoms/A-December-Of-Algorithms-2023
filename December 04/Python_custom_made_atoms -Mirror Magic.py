a = input("Enter the string: ")
l = []

for i in a:
    l.append(i)

l1 = len(l)
l2 = []

for i in range(l1-1,-1,-1):
    for j in range(0,l1):
        if l[i] == l[j] and i!=j:
            if l[i:(j+1)] != []:
                l2.append(l[i:(j+1)])

if l2 != []:
    print(l2[0])
else:
    print('No palindrome found')