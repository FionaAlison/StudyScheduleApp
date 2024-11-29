# app.py
from flask import Flask, request, jsonify
from models import db, Schedule
from config import Config
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

db.init_app(app)


@app.route('/schedules', methods=['GET'])
def get_schedules():
    schedules = Schedule.query.all()
    return jsonify([{
        "id": schedule.id,
        "title": schedule.title,
        "date": schedule.date,
        "time": schedule.time
    } for schedule in schedules])

@app.route('/schedules', methods=['POST'])
def add_schedule():
    data = request.json
    schedule = Schedule(title=data['title'], date=data['date'], time=data['time'])
    db.session.add(schedule)
    db.session.commit()
    return jsonify({"message": "Schedule added successfully!"}), 201

@app.route('/schedules/<int:id>', methods=['PUT'])
def update_schedule(id):
    data = request.json
    schedule = Schedule.query.get_or_404(id)
    schedule.title = data['title']
    schedule.date = data['date']
    schedule.time = data['time']
    db.session.commit()
    return jsonify({"message": "Schedule updated successfully!"})

@app.route('/schedules/<int:id>', methods=['DELETE'])
def delete_schedule(id):
    schedule = Schedule.query.get_or_404(id)
    db.session.delete(schedule)
    db.session.commit()
    return jsonify({"message": "Schedule deleted successfully!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5001)
