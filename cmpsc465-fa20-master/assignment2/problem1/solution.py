


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

# pairs = 0
# for i in range(len(array_B)):
#     for j in range(i+1, len(array_B)):
#         if (array_B[i] > array_B[j]):
#             pairs+=1
# print(pairs)
# print("\n\n")

# print(sortAndCount(array_B))
#1 5 -3 4 -6 -2 0 3


# = [1, 2, 3, 3, 4, 5, 6, 7]
print(sortAndCount(array_B)[0])