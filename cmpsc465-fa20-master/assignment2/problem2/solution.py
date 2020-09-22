import math
#Thanks to Matt, he helped us solve this algorithim out. We love you <3

def convexHull(points):
    n = len(points)
    if (n < 3):
        return("wtf")
    lUpper = [points[0], points[1]]
    for i in range(2, len(points)):
        lUpper.append(points[i])
        while(len(lUpper) > 2 and turningLeft(lUpper[-3:])):
            del lUpper[-2]

    lLower = [points[n-1],points[n-2]]
    for i in range(len(points)-3, -1, -1):
        lLower.append(points[i])
        while(len(lLower)>2 and turningLeft(lLower[-3:])):
            del lLower[-2]
    print(len(lLower),len(lUpper))

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
        bi = b[currentB][0]
        aj = a[currentA][1]
        bj = b[currentB][1]
        if (ai==bi):
            if (aj<=bj):
                mergedArray.append(a[currentA])
                currentA += 1
            else:
                mergedArray.append(b[currentB])
                currentB += 1
        elif (ai<bi):
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

numPoints = list(map(int, input().strip().split()))
points = []

for i in range(numPoints[0]):
    line = list(map(float, input().strip().split()))
    point = [line[0], -line[1]]
    points.append(point)
convexHull(sortAndCount(points))

