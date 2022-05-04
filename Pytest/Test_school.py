import pytest

from School import Students, School


@pytest.fixture(scope="class")
def student():
    sara = Students("Depp", 1, [10, 9, 9, 9, 10])
    school = School()
    school.add_student(sara)

    return school


class TestsSchool:

    def test_show_student_with_marks(self, student):
        assert len(student.show_student_with_marks(10, 9))

    def test_show_student_with_group(self, student):
        assert student.show_student_with_group(1)

    def test_show_students_with_automat(self, student):
        assert student.show_students_with_automat(9)


if __name__ == "__main__":
    pytest.main()
