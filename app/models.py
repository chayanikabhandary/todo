from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_description = db.Column(db.String(64), index=True)
    due_date = db.Column(db.Date, nullable= False)
    created_by = db.Column(db.String(128), nullable= False)
    status = db.Column(db.Boolean)
    deleted_by = db.Column(db.String(128))
    created_at = db.Column(db.Text, nullable= False)
    deleted_at = db.Column(db.Text, nullable= True)

    def __repr__(self):
        return '<Task {}>'.format(self.task_description)

     t= Task(task_description= 'Todo list', due_date= datetime.date(2018,01,30), created_by= 'Chayanika', created_at= datetime.date(2018,01,24))   