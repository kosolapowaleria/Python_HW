import pytest
from TeacherTable import TeacherTable

connection_string = 'postgresql://postgres:123@localhost:5432/postgres'


@pytest.fixture(scope="function")
def teacher_table():
    table = TeacherTable(connection_string=connection_string)
    yield table
    table.clear_all_teachers()


def test_add_teacher(teacher_table):
    teacher_id = 101
    email = 'test@mail.ru'
    group_id = 69

    teacher_table.create_teacher(teacher_id, email, group_id)
    teacher = teacher_table.get_teacher_by_id(teacher_id)

    assert len(teacher) == 1
    assert teacher[0]['email'] == email
    assert teacher[0]['group_id'] == group_id


def test_update_email(teacher_table):
    teacher_id = 102
    email = 'test@mail.ru'
    new_email = 'test_1@mail.ru'
    group_id = 81

    teacher_table.create_teacher(teacher_id, email, group_id)
    teacher_table.update_email(new_email, teacher_id)

    updated_teacher = teacher_table.get_teacher_by_id(teacher_id)
    assert updated_teacher[0]['email'] == new_email


def test_update_group(teacher_table):
    teacher_id = 103
    email = 'test@mail.ru'
    group_id = 81
    new_group_id = 178

    teacher_table.create_teacher(teacher_id, email, group_id)
    teacher_table.update_group(new_group_id, teacher_id)

    updated_group_id = teacher_table.get_teacher_by_id(teacher_id)
    assert updated_group_id[0]['group_id'] == new_group_id


def test_delete_teacher(teacher_table):
    teacher_id = 676
    email = 'gone@mail.ru'
    group_id = 123

    teacher_table.create_teacher(teacher_id, email, group_id)
    teacher_table.delete_teacher(teacher_id)

    deleted_teacher = teacher_table.get_teacher_by_id(teacher_id)
    assert len(deleted_teacher) == 0
