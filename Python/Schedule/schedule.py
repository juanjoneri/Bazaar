import pandas as pd
import numpy as np
from datetime import time
from datetime import datetime

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

    def __lt__(self, other):
        return self.name < other.name

class Schedule:
    units = 0
    _courses = []

    _labels = "| {:<30} | {:^5} | {:^8} | {:^8} |\n".format('Title','Days','Start T', 'End T')
    _separator = "|" + "-"*32 + "|" + "-"*7 + "|" + "-"*10 + "|" + "-"*10 + "|\n"

    def __init__(self, courses_data):
        self.name = self._labels + self._separator
        self.courses = courses_data
        self.units = sum([course.units for course in self.courses])

    def __str__(self):
        for course in self.courses:
            self.name += str(course)
        return self.name

    def __eq__(self, other):
        if self.units != other.units: return False
        for i in range(len(self.courses)):
            if self.courses[i] != other.courses[i]:
                return False
        return True

    def __lt__(self, other):
        return self.units > other.units

    @property
    def courses(self):
        return sorted(self._courses)

    @courses.setter
    def courses(self, courses_data):
        self._courses = []
        for course_data in courses_data:
            new_course = Course(*course_data)
            if new_course not in self._courses:
                self._courses.append(new_course)
                self.units += new_course.units

if __name__ == '__main__':
    classes = pd.read_csv('raw.csv', delimiter=',').values
    schedules = []
    # Build 20 random schedules that work, print only the uniques
    for i in range(100):
        schedule = Schedule(classes)
        if schedule not in schedules:
            schedules.append(schedule)
        np.random.shuffle(classes)

    for schedule in sorted(schedules):
        print(str(schedule), '\n| Units: ', schedule.units, '\n')
