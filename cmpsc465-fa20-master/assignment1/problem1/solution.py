
def mergeTwoSortedArrays(array1Size, array1, array2Size, array2):
    mergedArraySize = 0
    mergedArray = []
    pointer1 = 0
    pointer2 = 0
    for pointer in range(array1Size+array2Size):
        if pointer1 == array1Size:
            mergedArray.extend(array2[pointer2:])
            mergedArraySize += (array2Size-pointer2-1)
            break
        elif pointer2 == array2Size:
            mergedArray.extend(array1[pointer1:])
            mergedArraySize += (array1Size -pointer1-1)
            mergedArraySize += 1
            break
        if array1[pointer1] <= array2[pointer2]:
            mergedArray.append(array1[pointer1])
            pointer1+=1
            mergedArraySize+=1
        else:
            mergedArray.append(array2[pointer2])
            pointer2 += 1
            mergedArraySize += 1
    print(len(mergedArray), " ".join(map(str, mergedArray)))

array_A = list(map(int, input().strip().split()))  # takes integers input, puts them in list
len_A = array_A.pop(0)

array_B = list(map(int, input().strip().split()))  # takes integers input, puts them in list
len_B = array_B.pop(0)

mergeTwoSortedArrays(len_A, array_A, len_B, array_B)