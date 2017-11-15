from course import Course
from terminaltables import AsciiTable

class Schedule:
    units = 0
    _courses = []

    def __init__(self, courses_data):
        self.courses = courses_data

    def __str__(self):
        name = [Course._labels]
        name.extend([list(map(str, course.fields)) for course in self._courses])
        table = AsciiTable(name, str(self.units) + ' units')
        return table.table

    def __eq__(self, other):
        # when you order the courses in a schedule, al CRN should lign up
        for i in range(len(self.courses)):
            if not Course.same_course(self.courses[i], other.courses[i]):
                return False
        return True

    def __lt__(self, other):
        return self.units > other.units

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, courses_data):
        self._courses = []
        self.units = 0
        for course_data in courses_data:
            new_course = Course(*course_data)
            if new_course not in self._courses:
                self._courses.append(new_course)
                self.units += new_course.units
        self._courses.sort()

if __name__ == '__main__':
    classes = [
    '77216,Elements of Group Theory,MWF,02:25 pm-03:30 pm,4',
    '71624,Discrete Methods,MWF,10:25 am-11:15 am,3',
    '77231,Discrete Methods,MWF,11:35 am-12:25 pm,3',
    '72336,Operating Systems,TR,02:40 pm-04:10 pm,3',
    '73210,Lang Translation & Implement,TR,04:20 pm-05:50 pm,4',
    '77783,Artificial Intelligence,TR,11:20 am-12:50 pm,3',
    '76921,Theology and Science,R,04:20 pm-07:20 pm,4',
    '78921,Theology and Science,W,04:20 pm-07:20 pm,4',
    '75806,Computer System Design,W,06:00 pm-09:00 pm,3',
    '76625,Dance Conditioning: Pilates,TR,01:00 pm-02:30 pm,2']
    schedule = Schedule([clas.split(',') for clas in classes])
    print(schedule)
