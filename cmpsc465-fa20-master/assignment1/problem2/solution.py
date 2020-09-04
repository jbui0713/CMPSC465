
def mergeSort(inputArray):
    if len(inputArray)<= 1:
        return inputArray
    n = len(inputArray)//2
    inputArray1 = mergeSort(inputArray[:n])
    inputArray2 = mergeSort(inputArray[n:len(inputArray)])
    finalArray = mergeTwoSortedArrays(len(inputArray1), inputArray1, len(inputArray2), inputArray2)
    return finalArray

def mergeTwoSortedArrays(array1Size, array1, array2Size, array2):
    mergedArray = []
    pointer1 = 0
    pointer2 = 0
    for pointer in range(array1Size+array2Size):
        if pointer1 == array1Size:
            mergedArray.extend(array2[pointer2:])
            break
        elif pointer2 == array2Size:
            mergedArray.extend(array1[pointer1:])
            break
        if array1[pointer1] <= array2[pointer2]:
            mergedArray.append(array1[pointer1])
            pointer1+=1
        else:
            mergedArray.append(array2[pointer2])
            pointer2 += 1
    #print(len(mergedArray), " ".join(map(str, mergedArray)))
    return(mergedArray)

array_B = list(map(int, input().strip().split()))
array_A = list(map(int, input().strip().split()))  # takes integers input, puts them in list
print(" ".join(map(str, mergeSort(array_A))))
