from datetime import time
from datetime import datetime
from terminaltables import AsciiTable

class Course:
    """
    This object holds the information for a course, something like:
    77216,Elements of Group Theory,MWF,02:25 pm-03:30 pm,4
    Passed as strings, or not
    """

    _labels = ['CRN','Title','Days','Start T', 'End T']

    def __init__(self, CRN, name, days, time_rage, units):
        self.CRN = int(CRN)
        self.name = name
        self.days = list(days)
        self.time_range = time_rage #should this be a dict?
        self.units = int(units)

    def __str__(self):
        table = AsciiTable([self._labels, list(map(str, self.fields))])
        return table.table

    @property
    def fields(self):
        return tuple([self.CRN, self.name, '{:^5}'.format('-'.join(self.days)), *self.time_range])

    @property
    def time_range(self):
        # (14:25:00, 15:30:00)
        return self._time_range

    @time_range.setter
    def time_range(self, new_time_range):
        self._time_range = tuple(datetime.strptime(time_txt, '%I:%M %p').time() for time_txt in new_time_range.split("-"))

    @staticmethod
    def same_course(course1, course2):
        return course1.CRN == course2.CRN

    def __eq__(self, other):
        # Used to check if this course should be added or not:
        # 1. A course with the same name was added
        # 2. A course with overlapping times was added
        same_name = self.name == other.name
        overlapping_times = other.time_range[0] <= self.time_range[0] <= other.time_range[1]\
                     or  other.time_range[0] <= self.time_range[1] <= other.time_range[1]
        overlapping_days = any(set(self.days) & set(other.days))
        return same_name or (overlapping_times and overlapping_days)

    def __lt__(self, other):
        # Courses are ordered alphabetiaclly by name
        return self.name < other.name


if __name__ == '__main__':
    group_theory_sec_1_data = ['77216','Elements of Group Theory','MWF','02:25 pm-03:30 pm','4']
    group_theory_sec_2_data = ['77113','Elements of Group Theory','MWF','8:00 am-9:05 am','4']

    descrete_methods_data = ['71624','Discrete Methods','MW','8:30 am-9:45 am','3']

    group_theory_sec_1 = Course(*group_theory_sec_1_data)
    group_theory_sec_2 = Course(*group_theory_sec_2_data)

    descrete_methods = Course(*descrete_methods_data)

    print(group_theory_sec_1)
    print(group_theory_sec_2)

    print('Same ID ? ', Course.same_course(group_theory_sec_1, group_theory_sec_2))
    print('Everlaping schedule? ', group_theory_sec_1 == group_theory_sec_2)

    print(descrete_methods)

    print('Overlaps with GT section 1? ', group_theory_sec_1 == descrete_methods)
    print('Overlaps with GT section 2? ', group_theory_sec_2 == descrete_methods)
