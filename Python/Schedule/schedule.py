import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime
import re

class Course:

    def __init__(self, CRN, name, days, time_rage, units):
        self.CRN = id
        self.name = name
        self.days = list(days)
        self.time_range = time_rage
        self.units = units

    def __str__(self):
        return "| {:<30} | {:^5} | {:>7} | {:>7} |\n".format(self.name, '-'.join(self.days), str(self.time_range[0]), str(self.time_range[1]))

    @property
    def time_range(self):
        return self._time_range

    @time_range.setter
    def time_range(self, new_time):
        start_t, end_t = new_time.split("-")
        start_obj = datetime.strptime(start_t, '%I:%M %p')
        end_obj = datetime.strptime(end_t, '%I:%M %p')
        self._time_range = (start_obj.time(), end_obj.time())

    def __eq__(self, other):
        same_class = self.name == other.name
        same_times = other.time_range[0] <= self.time_range[0] <= other.time_range[1]
        overlapping_days = any(set(self.days) & set(other.days))
        return same_class or (same_times and overlapping_days)

class Schedule:
    _courses = []
    units = 0

    _labels = "| {:<30} | {:^5} | {:^8} | {:^8} |\n".format('Title','Days','Start T', 'End T')
    _separator = "|" + "-"*32 + "|" + "-"*7 + "|" + "-"*10 + "|" + "-"*10 + "|\n"

    def __init__(self, courses_data):
        self.name = self._labels + self._separator
        self.courses = courses_data
        self.units = sum([course.units for course in self.courses])

    def __str__(self):
        return self.name

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, courses_data):
        for course_data in courses_data:
            new_course = Course(*course_data)
            if new_course not in self._courses:
                self.courses.append(new_course)
                self.units += new_course.units
                self.name += str(new_course)

if __name__ == '__main__':
    # Save your classes in order of priority and I will create a schedule for you...
    df = pd.read_csv('raw.csv', delimiter=',')
    courses = []
    units = 0

    schedule = Schedule(df.values)
    print(str(schedule))
    print(schedule.units)
