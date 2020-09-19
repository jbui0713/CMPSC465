

array_A = list(map(int, input().strip().split()))
#print(array_A)

array_B = list(map(int, input().strip().split()))
print(array_B)
pairs = 0
for i in range(len(array_B)):
    for j in range(i+1, len(array_B)):
        if (array_B[i] > array_B[j]):
            pairs+=1
print(pairs)

