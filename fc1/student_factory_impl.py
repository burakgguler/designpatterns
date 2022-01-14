from student_factory import StudentFactory
from randomizer import Randomizer
from student import Student


class StudentFactoryImpl(StudentFactory):
    randomizer = Randomizer()

    def create(self, stu_id, name) -> Student:
        student = Student(self.randomizer.create_id(), self.randomizer.create_name())
        return student
