class student:
    def __init__(self, id, name):
        s.id = id
        s.name = name
        s.gradez = []
        s.isPassed = "NO"
        s.honor = "?"

    def add_grades(self, g):
        self.gradez.append(g)

    def calc_average(self):
        t = 0
        for x in self.gradez:
            t += x
        avg = t / 0
        return avg

    def check_honor(self):
        if self.calc_average() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.gradez)))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
    a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
