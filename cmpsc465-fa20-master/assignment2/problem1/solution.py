def mergeAndCount(a, b):
    currentA = 0
    currentB = 0
    count = 0
    mergedArray = []
    while((currentA < len(a)) & (currentB < len(b))):
        ai = a[currentA]
        bj = b[currentB]
        if (ai<=bj):
            mergedArray.append(ai)
            currentA += 1
        else:
            mergedArray.append(bj)
            count+=(len(a)-currentA)
            currentB += 1
    if(currentA == len(a)):
        mergedArray.extend(b[currentB:])
    else:
        mergedArray.extend(a[currentA:])
    return(count, mergedArray)

def sortAndCount(l):
    ra = 0
    rb = 0
    r = 0
    if(len(l)<=1):
        pass
    else:
        n = len(l) // 2
        a = l[:n]
        b = l[n:len(l)]
        (ra, a) = sortAndCount(a)
        (rb, b) = sortAndCount(b)
        (r, l) = mergeAndCount(a,b)
    r = ra+rb+r
    return (r, l)


array_A = list(map(int, input().strip().split()))
length = array_A[0]

array_B = list(map(int, input().strip().split()))

print(sortAndCount(array_B)[0])