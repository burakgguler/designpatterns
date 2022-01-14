from master_student import MasterStudent


class PhdStudent(MasterStudent):
    def __init__(self, stu_id, name, department, year):
        super().__init__(stu_id, name, department)
        self.year = year
