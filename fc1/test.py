from student_affairs import StudentAffairs
from student_factory_impl import StudentFactoryImpl
from master_student_factory_impl import MasterStudentFactoryImpl
from phd_student_factory_impl import PhdStudentFactoryImpl


class Test:
    affair = StudentAffairs()

    student_factory = StudentFactoryImpl(1, "Gözde")
    master_student_factory = MasterStudentFactoryImpl(2, "İlhan", "Psychology")
    phd_student_factory = PhdStudentFactoryImpl(3, "Hülya", "Art", 4)

    affair.add_new_students(student_factory.create(2, "Ali"))
    affair.add_new_students(student_factory.create(3, "Ayşe"))
    affair.add_new_students(master_student_factory.create(4, "Berkecan", "Computer Science"))
    affair.add_new_students(phd_student_factory.create(5, "Emre", "Logistics", 4))

    for student in affair.students:
        print(student.stu_id)
        print(student.name)
