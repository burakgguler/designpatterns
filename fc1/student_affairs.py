class StudentAffairs:
    students = []

    def get_students(self):
        return self.students

    def get_number_of_students(self):
        return len(self.students)

    def add_new_students(self, student):
        self.students.append(student)

    def list_students(self):
        print('Listing all students...')
        for student in self.students:
            print(student)