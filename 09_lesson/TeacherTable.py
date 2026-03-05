from sqlalchemy import create_engine, text


class TeacherTable:
    __scripts = {
        'select': text('SELECT * FROM teacher'),
        'select_by_id': text(
            'SELECT * FROM teacher '
            'WHERE teacher_id = :selected_id'
        ),
        'insert': text(
            'INSERT INTO teacher ("teacher_id", "email", "group_id") '
            'VALUES (:new_teacher_id, :new_email, :group_id)'
        ),
        'delete_by_id': text(
            'DELETE FROM teacher '
            'WHERE teacher_id = :id_to_delete'
        ),
        'update_email': text(
            'UPDATE teacher SET email = :new_email '
            'WHERE teacher_id = :selected_id'
        ),
        'update_group': text(
            'UPDATE teacher SET group_id = :new_group_id '
            'WHERE teacher_id = :selected_id'
        )
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_teacher(self):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts['select']
        )
        rows = result.mappings().all()
        conn.close()
        return rows

    def create_teacher(self, teacher_id, email, group_id):
        conn = self.__db.connect()
        conn.execute(self.__scripts['insert'],
                     {'new_teacher_id': teacher_id,
                      'new_email': email,
                      'group_id': group_id})
        conn.commit()
        conn.close()

    def get_teacher_by_id(self, id):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts['select_by_id'],
            {'selected_id': id}
        )
        teacher = result.mappings().all()
        conn.close()
        return teacher

    def update_email(self, new_email, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts['update_email'],
                     {'new_email': new_email,
                      'selected_id': id})
        conn.commit()
        conn.close()

    def update_group(self, new_group_id, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts['update_group'],
                     {'new_group_id': new_group_id,
                      'selected_id': id})
        conn.commit()
        conn.close()

    def delete_teacher(self, id):
        conn = self.__db.connect()
        conn.execute(self.__scripts['delete_by_id'],
                     {'id_to_delete': id})
        conn.commit()
        conn.close()

    def clear_all_teachers(self):
        conn = self.__db.connect()
        conn.execute(text("DELETE FROM teacher"))
        conn.commit()
        conn.close()
