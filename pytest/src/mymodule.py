listone = [2,12,1,10, 3, 4]
listtwo = [2*i for i in listone if i > 2]
list3 = list()
for i in listone: 
    if i>2:
        j = 2*i
    else:
        j=i
    list3.append(j)
print list3, listtwo