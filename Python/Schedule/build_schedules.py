import pandas as pd
import numpy as np
from schedule import Schedule

if __name__ == '__main__':
    classes = pd.read_csv('raw.csv', delimiter=',').values
    schedules = []
    delta = 30 # i know this is bad

    while delta > 0:
        schedule = Schedule(classes)
        if schedule not in schedules:
            schedules.append(schedule)
            delta = 30
        else:
            delta -= 1
        np.random.shuffle(classes)

    for schedule in sorted(schedules):
        print(str(schedule), '\n')
