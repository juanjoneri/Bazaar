from time import sleep
from random import randint
from math import ceil
import os

rows, columns = os.popen('stty size', 'r').read().split()
modoVisual = int(input("modo visual? [1/2] >>  ") or "1")

center = ceil(int(columns)/2)
position = 0
average = 0
numOfSteps = int(input("steps? [30] >> ") or "30")
string = ""

for i in range(numOfSteps):
    average += abs(position)
    string = ""

    if modoVisual == 1:
        if position < 0:
            for j in range(center + position):
                string += " "
            for j in range(-position):
                string += "-"
        else:
            for j in range(center):
                string += " "
            for j in range(position):
                string += "-"

    elif modoVisual == 2:
        if position < 0:
            for j in range(center + position):
                string += " "
            string += "0"
            for j in range(-position - 1):
                string += " "
            string += "|"
        else:
            for j in range(center):
                string += " "
            string += "|"
            for j in range(position - 1):
                string += " "
            string += "0"

    print(string)
    step = randint(0,1)
    position = position + 1 if step == 1 else position - 1

    sleep(0.01)

print("# the average was -> {}".format(ceil(average/numOfSteps)))
