from master_student_factory import MasterStudentFactory
from master_student import MasterStudent
from randomizer import Randomizer


class MasterStudentFactoryImpl(MasterStudentFactory):
    randomizer = Randomizer()

    def create(self, stu_id, name, department) -> MasterStudent:
        master_student = MasterStudent(self.randomizer.create_id(), self.randomizer.create_name(),
                                       self.randomizer.create_dept())
        return master_student
