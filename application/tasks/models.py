from application import db
from application.models import Base

from sqlalchemy.sql import text

class Task(Base):

    name = db.Column(db.String(144), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)

    def __init__(self, name):
        self.name = name
        self.done = False

    @staticmethod # total number of tasks, all users
    def total_number_of_tasks():
        stmt = text("SELECT COUNT()"
                    "FROM Task;")
        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"total":row[0]})
        return response
