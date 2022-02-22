from functools import reduce
import math
srcData = [139, 1774, 846, 282, 836, 704, 92, 50, 478,
           573, 311, 1466, 125, 181, 206, 270, 394,
           1854, 39, 34, 425, 631, 361, 115, 841, 1139,
           191, 677, 944, 401, 269, 735, 235, 148, 74,
           371, 324, 635, 421, 925, 195, 229, 276,
           1184, 172, 1017, 323, 658, 183, 769, 516,
           364, 1301, 1699, 71, 74, 143, 1885, 505, 70,
           249, 408, 224, 17, 1197, 86, 834, 127, 121,
           794, 144, 325, 251, 863, 75, 1078, 98, 114,
           226, 489, 250, 323, 505, 0, 151, 219, 169,
           177, 456, 43, 400, 142, 1754, 110, 540, 756,
           1605, 195, 593, 103]
gamma = 0.89
t1 = 645
t2 = 601
numberOfIntervals = 10

correctValues = True if gamma < 1 and gamma > 0 and len(
    srcData) > 0 and numberOfIntervals > 0 else False
if correctValues:
    srcData.sort()
    T_average = sum(srcData) / len(srcData)

    h = srcData[-1] / numberOfIntervals
    intervalValues = [list(filter(lambda x: x > i*h and x < (i+1)*h, srcData)) for i, x in enumerate([
        None] * numberOfIntervals)]

    fi = list(map(lambda x: len(x) / (len(srcData) * h), intervalValues))

    p = []
    for i in range(len(fi)):
        p.append(1 - ((fi[i] * h) + (1 - p[i - 1] if i > 0 else 0)))

    pIndex = 0
    for i in range(len(p)):
        if gamma <= p[i] and gamma > p[i + 1]:
            pIndex = i
            break

    if (pIndex == 0):
        t = 0 + h * ((1 - gamma) / (1 - p[0]))
    else:
        t = intervalValues[pIndex][0] + h * \
            ((p[pIndex+1]-gamma)/(p[pIndex+1]-p[pIndex]))

    arr = [None] * math.ceil(t1 / h)
    t1Interval = math.ceil(t1 / h)
    pT1 = 1 - reduce(lambda x, y: x + y, [fi[i] * h if i < (t1Interval - 1) else (t1 - h * (t1Interval-1))*fi[i] for i, x in enumerate([
        None] * t1Interval)], 0)

    i = 0
    index = 0
    λ = fi[math.ceil(t2 / h) - 1] / pT1

    print("Intervals")
    for i in range(numberOfIntervals):
        print("\t {} -- {}".format(i * h, (i + 1) * h))

    print("T average: {} \n"
          "T({:.2f}) = {:.2f} \n"
          "Non-failure for {:.2f} = {:.5f} \n"
          "λ({}) = {:.7f}".format(T_average, gamma, t, t1, pT1, t2, λ))
else:
    print("You entered wrong data. Check your input and try again")

print("p:")
for i in p:
    print("{:.3f}".format(i))
print('======================')
print("f:")
for i in fi:
    print("{:.5f}".format(i))
