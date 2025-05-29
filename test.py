class Student:
    def __init__(self, student_id, name):
        if not student_id or not name:
            raise ValueError("ID and name must not be empty.")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.honor_roll = False
        self.passed = False

    def add_grade(self, grade):
        if not isinstance(grade, (int, float)):
            print("Error: Grade must be a number.")
            return
        if not (0 <= grade <= 100):
            print("Error: Grade must be between 0 and 100.")
            return
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def determine_pass_fail(self):
        avg = self.calculate_average()
        self.passed = avg >= 60
        return "Passed" if self.passed else "Failed"

    def check_honor_roll(self):
        avg = self.calculate_average()
        self.honor_roll = avg >= 90
        return self.honor_roll

    def remove_grade(self, value=None, index=None):
        try:
            if value is not None:
                self.grades.remove(value)
            elif index is not None:
                del self.grades[index]
            else:
                print("Error: Provide either value or index to remove a grade.")
        except (ValueError, IndexError):
            print("Error: Grade not found or index out of bounds.")

    def generate_report(self):
        print("📄 Student Summary Report")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Grades: {self.grades}")
        avg = self.calculate_average()
        print(f"Average Grade: {avg:.2f}")
        print(f"Letter Grade: {self.determine_letter_grade()}")
        print(f"Status: {self.determine_pass_fail()}")
        print(f"Honor Roll: {'Yes' if self.check_honor_roll() else 'No'}")

def start_run():
    student1 = Student("001", "Alice")
    student1.add_grade(95.0)
    student1.add_grade(85.0)
    student1.add_grade("Fifty")  # Invalid
    student1.add_grade(105)      # Invalid
    student1.remove_grade(index=5)  # IndexError handled
    student1.generate_report()

if __name__ == "__main__":
    start_run()
