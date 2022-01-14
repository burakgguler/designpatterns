from student import Student


class MasterStudent(Student):
    def __init__(self, stu_id, name, department):
        super().__init__(stu_id, name)
        self.department = department
