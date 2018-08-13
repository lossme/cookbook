from .. import db
from ..exceptions import ParamError


class Todo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    message = db.Column(db.String(1024))

    def export(self):
        return {
            'id': self.id,
            'message': self.message
        }

    @staticmethod
    def add(message):
        todo = Todo(message=message)
        db.session.add(todo)
        db.session.commit()
        return todo.export()

    @staticmethod
    def delete(id):
        todo = db.session.query(Todo).filter_by(id=id).first()
        if not todo:
            raise ParamError('未找到对应的id')
        db.session.delete(todo)
        db.session.commit()
        return {'id': id}

    @staticmethod
    def list():
        todo_list = db.session.query(Todo)
        return [todo.export() for todo in todo_list]
