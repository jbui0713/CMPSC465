import math

def convexHull(points):
    n = len(points)
    if (n < 3):
        return("wtf")
    lUpper = [points[0], points[1]]
    for i in range(2, len(points)):
        lUpper.append(points[i])
       # print(str(lUpper[-3:]))
        while(len(lUpper) > 2 and turningLeft(lUpper[-3:])):
            del lUpper[-2]

    lLower = [points[n-1],points[n-2]]
    for i in range(len(points)-3, 0, -1):
        lLower.append(points[i])
        while(len(lLower)>2 and turningLeft(lLower[-3:])):
            del lLower[-2]
    del lLower[0]
    del lLower[-1]
    print(lUpper)
    print(lLower)
    # for

def combine():
    pass

def turningLeft(points):
    x12 = points[1][0] - points[0][0]
    x23 = points[2][0] - points[1][0]
    y12 = points[1][1] - points[0][1]
    y23 = points[2][1] - points[1][1]
    dirChange = (math.atan2(x12 * y23 - x23 * y12, x12 * x23 + y12 * y23))*180/math.pi
    if (dirChange >= 0):
        return(1)
    else:
        return(0)

def merge(a, b):

    currentA = 0
    currentB = 0
    mergedArray = []
    while((currentA < len(a)) & (currentB < len(b))):
        ai = a[currentA][0]
        bj = b[currentB][0]
        if (ai<=bj):
            mergedArray.append(a[currentA])
            currentA += 1
        else:
            mergedArray.append(b[currentB])
            currentB += 1
    if(currentA == len(a)):
        mergedArray.extend(b[currentB:])
    else:
        mergedArray.extend(a[currentA:])
    return(mergedArray)

def sortAndCount(l):
    if(len(l)<=1):
        pass
    else:
        n = len(l) // 2
        a = l[:n]
        b = l[n:len(l)]
        a = sortAndCount(a)
        b = sortAndCount(b)
        l = merge(a,b)
    return (l)

#turningLeft([[0,0],[0,2],[-1,0]])
#
numPoints = list(map(int, input().strip().split()))
points = []

for i in range(numPoints[0]):
    point = list(map(float, input().strip().split()))
    points.append(point)
convexHull(sortAndCount(points))
# print(sortAndCount(points))
