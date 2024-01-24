def fakultaet(x):
    if (x == 1):
        return 1
    else:
        return fakultaet(x-1)*x
    
for i in range(1,7):
    print (fakultaet(i))

