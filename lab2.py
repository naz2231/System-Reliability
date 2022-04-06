from copy import copy, deepcopy
from math import log

possibil = [0.97, 0.06, 0.13, 0.35, 0.31, 0.48, 0.51]
matrix = [[0, 1, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]


def lab2(possibilities, matrix):
    for i in possibilities:
        if i < 0 or i > 1:
            print("Wrong possibility")
            exit(1)

    n = len(possibilities)
    if n < 1:
        print("Empty matrix")
        exit(1)
    if len(matrix) != n:
        print("Wrong links")
        exit(1)
    else:
        for i in matrix:
            if i.count(True) + i.count(False) != n:
                print("Wrong links")
                exit(1)

    transposedMatrix = list(zip(*matrix))
    startNodes = []
    endNodes = []
    for i in range(len(transposedMatrix)):
        # if column contains only 0 -- it's a start point
        if transposedMatrix[i].count(False) == n:
            startNodes.append(i)
    for i in range(len(matrix)):
        if matrix[i].count(False) == n:  # if row only 0 -- end point
            endNodes.append(i)
    if not startNodes or not endNodes:
        print("No start or end element")
        exit(1)

    ways = []
    way = []

    def findWays(node, previousNode):
        if previousNode != n:
            if matrix[node][previousNode:].count(True) > 0:
                index = matrix[node].index(True, previousNode)
                way.append(index)
                findWays(index, 0)
            else:
                if matrix[node].count(False) == n:
                    ways.append(copy(way))
                    # print([_ + 1 for _ in way])
                way.remove(node)
                if way:
                    findWays(way[-1], node + 1)
        else:
            way.remove(node)
            if way:
                findWays(way[-1], node + 1)
        # print(ways)
        # print(matrix)

    def breakOrNot(a, b):
        if a == 0:
            return 1 - b
        if a == 1:
            return b

    def composition(massive):
        result = 1
        for elem in massive:
            result *= elem
        return result

    if n == 1:
        possibility = possibilities[0]
    else:
        for i in startNodes:
            way.append(i)
            findWays(i, 0)
        if not ways:
            print("No ways found")
            exit(1)

        else:
            goodWays = []
            for i in ways:
                goodStates = [[]]
                for j in range(n):
                    if j in i:
                        for k in range(len(goodStates)):
                            goodStates[k].append(1)
                    else:
                        goodStates.extend(deepcopy(goodStates))
                        for k in range(int(len(goodStates) / 2)):
                            goodStates[k].append(0)
                            goodStates[-k - 1].append(1)
                for k in goodStates:
                    if k not in goodWays:
                        goodWays.append(k)
            possibility = 0
            for i in goodWays:
                possibility += composition(list(map(breakOrNot,
                                                    i, possibilities)))
    return possibility


def main():
    print("Імовірність безвідмовної роботи системи протягом 10 годин = {}".format(
        lab2(possibil, matrix)))


main()
