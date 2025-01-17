from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    dueDate = db.Column(db.DateTime, nullable=False)

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'text': task.text, 'completed': task.completed, 'dueDate': task.dueDate} for task in tasks])

@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(text=data['text'], dueDate=datetime.strptime(data['dueDate'], '%Y-%m-%d %H:%M:%S'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'text': new_task.text, 'completed': new_task.completed, 'dueDate': new_task.dueDate})

@app.route('/api/tasks/<int:id>/complete', methods=['POST'])
def complete_task(id):
    task = Task.query.get(id)
    if task:
        task.completed = True
        db.session.commit()
        return jsonify({'id': task.id, 'text': task.text, 'completed': task.completed, 'dueDate': task.dueDate})
    return jsonify({'error': 'Task not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
