from phd_student_factory import PhdStudentFactory
from phd_student import PhdStudent
from randomizer import Randomizer


class PhdStudentFactoryImpl(PhdStudentFactory):
    randomizer = Randomizer()

    def create(self, stu_id, name, department, year) -> PhdStudent:
        phd_student = PhdStudent(self.randomizer.create_id(), self.randomizer.create_name(),
                                 self.randomizer.create_dept(), self.randomizer.create_year())
        return phd_student
