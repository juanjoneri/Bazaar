import sys
import re
import collections
import datetime
from copy import deepcopy

class DataPoint(object):
    """
    Each member of this class represents a data point
    with a date and a list of engagement dictionaries (type, count)
    """
    _engagements = {} # One point can have multiple engagements, stored as dictionaries

    def __init__(self, date, *engagements):
        self.date = date
        self.engagements = engagements #go through the setter

    # return them as it would be expected from the constructor
    @property
    def engagements(self):
        return self._engagements.items()

    # engagements should be provided as in constructor: al list of (type, count) touples
    @engagements.setter
    def engagements(self, new_engagements):
        self._engagements = dict(new_engagements)

    def __str__(self):
        self._name = '{0:%Y}-{0:%m}'.format(self.date)
        for e_type, e_count in sorted(self._engagements.items(), key=lambda e: e[0]):
            # Sorted by key
            self._name += ', {}, {}'.format(e_type, e_count)
        return self._name

    # Used to select the correct range to print out
    def __lt__(self, other):
        if self.date == other.date:
            return 0
        return self.date < other.date

    # We are cheating here, but if month and year are the same, then points are equal
    # Since they should be combined
    def __eq__(self, other):
        return self.date.year == other.date.year \
        and self.date.month == other.date.month

    # Returns a new point representing the combination of the provided points
    # With engagements being the union of all the engagements
    @staticmethod
    def combine(*data_points):
        combination_date = data_points[0].date
        combination_engagements = []
        for data_point in data_points:
            combination_engagements.extend(data_point.engagements)

        return DataPoint(combination_date, *combination_engagements)

data_point_pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})[ ]*,[ ]*(\w+)[ ]*,[ ]*(\d+)\n')
date_pattern = re.compile(r'(\d+)-(\d+)')
# Thoroughly tested here: https://regex101.com/r/4zPpxb/2

def parse_date_interval(line):
    start, end = date_pattern.findall(line)
    start = tuple(map(int, start))
    end = tuple(map(int, end))
    return datetime.date(*start, 1), datetime.date(*end, 1) # date needs a day, just pass 1

def parse_data_point(line):
    if data_point_pattern.match(line):
        fields = data_point_pattern.match(line).groups()
        date = datetime.date(*tuple(map(int, fields[:3])))
        engagement = fields[3], int(fields[4])
        return date, engagement
    else:
        raise ValueError('line does not fit data point pattern')


def combine_repetitions(structure):
    combined_structure = []
    for point in structure:
        if point not in combined_structure:
            combination = DataPoint.combine(*[p for p in structure if p == point])
            combined_structure.append(combination)
    return combined_structure

if __name__ == '__main__':
    start, end = parse_date_interval(sys.stdin.readline())
    time_series = []
    repeated = []


    for line in sys.stdin:
        try:
            new_point = DataPoint(*parse_data_point(line))
            time_series.append(new_point)
        except ValueError:
            continue

    time_series = combine_repetitions(time_series)
    correct_range = [point for point in reversed(sorted(time_series)) if start < point.date < end]

    for point in correct_range:
        print(point)
