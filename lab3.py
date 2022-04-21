import lab2
from math import log, factorial

possibilities = [0.97, 0.06, 0.13, 0.35, 0.31, 0.48, 0.51]
matrix = [[0, 1, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 1],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0]]

t = 1809
k1 = 2
k2 = 2

possibility = lab2.lab2(possibilities, matrix)
qssibility = 1 - possibility
tAvrg = -t / log(possibility)
print("Базова імовірність безвідмовної роботи = {}\n"
      "Базова імовірність відмови = {}\n"
      "Базовий середній наробіток на відмову = {}\n".format(possibility, qssibility, tAvrg))


def loadedjoint(t, k, qssib, possib, taver):
    q1 = pow(qssib, (k + 1))
    p1 = 1 - q1
    taver1 = -t / log(p1)
    gq1 = q1 / qssib
    gp1 = p1 / possib
    gt1 = taver1 / taver
    print("Імовірність безвідмовної роботи системи з навантаженим загальним резервуванням = {}\n"
          "Імовірність відмови системи з навантаженим загальним резервуванням = {}\n"
          "Середній час роботи системи з навантаженим загальним резервуванням = {}".format(p1, q1, taver1))
    print("Виграш системи з навантаженим загальним резервуванням по імовірності безвідмовної роботи = {}\n"
          "Виграш системи з навантаженим загальним резервуванням по імовірності відмови = {}\n"
          "Виграш системи з навантаженим загальним резервуванням по середньому часу роботи = {}\n".format(gp1, gq1, gt1))


def notloadedjoint(t, k, qssib, possib, taver):
    q1 = pow(qssib, (k + 1)) / factorial(k + 1)
    p1 = 1 - q1
    taver1 = -t / log(p1)
    gq1 = q1 / qssib
    gp1 = p1 / possib
    gt1 = taver1 / taver
    print("Імовірність безвідмовної роботи системи з ненавантаженим загальним резервуванням = {}\n"
          "Імовірність відмови системи з ненавантаженим загальним резервуванням = {}\n"
          "Середній час роботи системи з ненавантаженим загальним резервуванням = {}".format(p1, q1, taver1))
    print("Виграш системи з ненавантаженим загальним резервуванням по імовірності безвідмовної роботи = {}\n"
          "Виграш системи з ненавантаженим загальним резервуванням по імовірності відмови = {}\n"
          "Виграш системи з ненавантаженим загальним резервуванням по середньому часу роботи = {}\n".format(gp1, gq1, gt1))


def loadeddistributed(t, k, qssib, poss, possib, taver, linkmat):
    newpossibilities = list(map(lambda x: 1 - (1 - x) ** (k + 1), possib))
    p2 = lab2.lab2(newpossibilities, linkmat)
    q2 = 1 - p2
    taver2 = -t / log(p2)
    gq2 = q2 / qssib
    gp2 = p2 / poss
    gt2 = taver2 / taver
    print("Імовірність безвідмовної роботи системи з навантаженим розподіленим резервуванням = {}\n"
          "Імовірність відмови системи з навантаженим розподіленим резервуванням = {}\n"
          "Середній час роботи системи з навантаженим розподіленим резервуванням = {}".format(p2, q2, taver2))
    print("Виграш системи з навантаженим розподіленим резервуванням по імовірності безвідмовної роботи = {}\n"
          "Виграш системи з навантаженим розподіленим резервуванням по імовірності відмови = {}\n"
          "Виграш системи з навантаженим розподіленим резервуванням по середньому часу роботи = {}\n".format(gp2, gq2, gt2))


def notloadeddistributed(t, k, qssib, poss, possib, taver, linkmat):
    newpossibilities = list(
        map(lambda x: 1 - (1 - x) ** (k + 1) / factorial(k + 1), possib))
    p2 = lab2.lab2(newpossibilities, linkmat)
    q2 = 1 - p2
    taver2 = -t / log(p2)
    gq2 = q2 / qssib
    gp2 = p2 / poss
    gt2 = taver2 / taver
    print("Імовірність безвідмовної роботи системи з ненавантаженим розподіленим резервуванням = {}\n"
          "Імовірність відмови системи з ненавантаженим розподіленим резервуванням = {}\n"
          "Середній час роботи системи з ненавантаженим розподіленим резервуванням = {}".format(p2, q2, taver2))
    print("Виграш системи з ненавантаженим розподіленим резервуванням по імовірності безвідмовної роботи = {}\n"
          "Виграш системи з ненавантаженим розподіленим резервуванням по імовірності відмови = {}\n"
          "Виграш системи з ненавантаженим розподіленим резервуванням по середньому часу роботи = {}\n".format(gp2, gq2, gt2))


loadedjoint(t, k1, qssibility, possibility, tAvrg)
notloadedjoint(t, k1, qssibility, possibility, tAvrg)
loadeddistributed(t, k2, qssibility, possibility,
                  possibilities, tAvrg, matrix)
notloadeddistributed(t, k2, qssibility, possibility,
                     possibilities, tAvrg, matrix)
