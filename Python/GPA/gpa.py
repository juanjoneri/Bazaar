import numpy as np
from sys import stdin

def calculate_gpa(scores):
    TPE = TCA = 0
    for units, score in scores:
        TPE += units * score
        TCA += units
    return round(TPE / TCA, 2)

scale = {'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7, 'c+': 2.3, 'C': 2, 'C-': 1.7, 'D+': 1.3, 'D': 1}

if __name__ == '__main__':
    
    class_data = np.array([line.rstrip().split(sep=', ') for line in stdin if line != '\n'])
    
    categories = set(class_data[:,0])
    
    for category in categories:
        scores = [(int(units), scale[letter]) for cat, name, units, letter in class_data if cat == category]
        print(f'{category}: {calculate_gpa(scores)}')