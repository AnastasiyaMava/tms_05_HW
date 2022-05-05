import pytest

from School import Students, School


@pytest.fixture(scope="class")
def student():
    sara = Students("Depp", 1, [10, 9, 9, 9, 10])
    nikita = Students("Ronaldo", 2, [5, 6, 6, 5, 6])
    school = School()
    school.add_student(sara)
    school.add_student(nikita)
    return school


@pytest.mark.pozitive
class Test_pozitive:
    def test_show_student_with_marks(self):
        pass

    def test_show_student_with_group(self):
        pass

    def test_show_students_with_automat(self):
        pass


@pytest.mark.negative
class Test_negative:
    def test_show_student_with_marks_neg(self):
        pass

    def test_show_student_with_group_neg(self):
        pass

    def test_show_students_with_automat_neg(self):
        pass


class School_pozitive:

    def test_show_student_with_marks(self, student):
        mark = student.show_student_with_marks(10, 9)
        assert mark == "Student Depp in the 1 group has only (10, 9) marks"

    def test_show_student_with_group(self, student):
        group = student.show_student_with_group(1)
        assert group == 'Student Depp in the group 1'

    def test_show_students_with_automat(self, student):
        automat = student.show_students_with_automat(7)
        assert automat == 'Student Depp has automat'


class School_negative:

    def test_show_student_with_marks_neg(self, student):
        marks = student.show_student_with_marks(5, 6)
        assert marks != 'Student Ronaldo in the 2 group has only (10, 9) marks'

    def test_show_student_with_group_neg(self, student):
        group = student.show_student_with_group(2)
        assert group != 'Student Ronaldo in the group 1'

    def test_show_students_with_automat_neg(self, student):
        automat = student.show_students_with_automat(7)
        assert automat != 'Student Ronaldo has automat'


if __name__ == "__main__":
    pytest.main()
