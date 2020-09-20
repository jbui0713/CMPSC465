


def mergeAndCount(a, b):
    currentA = 0
    currentB = 0
    count = 0
    removeB = []
    mergedArray = []
    while((currentA < len(a)) & (currentB < len(b))):
        ai = a[currentA]
        bj = b[currentB]
        if (ai<bj):
            mergedArray.append(ai)
            currentA += 1
        else:
            mergedArray.append(bj)
            count+=(len(a)-currentA)
            removeB.append(bj)
            currentB += 1
<<<<<<< HEAD
    if(currentA == len(a)):
        mergedArray.extend(b[currentB:])
=======
        #print(mergedArray)
    if(currentA == len(a)):
        newB = [i for i in b if i not in removeB]
        mergedArray.extend(newB)
>>>>>>> origin/master
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
<<<<<<< HEAD
        (rb, b) = sortAndCount(b)
        (r, l) = mergeAndCount(a,b)
=======
        #print(a)
        (rb, b) = sortAndCount(b)
        #print(b)
        (r, l) = mergeAndCount(a,b)
        #print(l)
>>>>>>> origin/master
    r = ra+rb+r
    return (r, l)


<<<<<<< HEAD
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
=======
array_A = int(input())

array_B = list(map(int, input().strip().split()))

#print(sortAndCount(array_B))

#a = [1, 2, 3, 5]
#b = [3, 4, 6, 7]
# = [1, 2, 3, 3, 4, 5, 6, 7]
#print(mergeAndCount(a,b))

# Python 3 program to count inversions in an array

# Function to Use Inversion Count
def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)

def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0

    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(arr, temp_arr, left, mid)
        inv_count += _mergeSort(arr, temp_arr, mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return inv_count


result = mergeSort(array_B, array_A)
print(result)
>>>>>>> origin/master
