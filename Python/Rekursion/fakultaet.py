def faculty(x):
    if (x == 1):
        return 1
    else:
        return faculty(x-1)*x
    
for i in range(1,7):
    print (faculty(i))

