import os
from flask import Flask, request, jsonify
from models import db, Schedule, Quote
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database connection
db.init_app(app)

@app.route('/schedules', methods=['GET', 'POST'])
def manage_schedules():
    if request.method == 'GET':
        schedules = Schedule.query.all()
        return jsonify([{"id": s.id, "title": s.title, "date": s.date, "time": s.time} for s in schedules]), 200

    elif request.method == 'POST':
        data = request.json
        new_schedule = Schedule(title=data['title'], date=data['date'], time=data['time'])
        db.session.add(new_schedule)
        db.session.commit()
        return jsonify({"message": "Schedule created", "id": new_schedule.id}), 201

@app.route('/schedules/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_schedule(id):
    schedule = Schedule.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify({"id": schedule.id, "title": schedule.title, "date": schedule.date, "time": schedule.time}), 200

    elif request.method == 'PUT':
        data = request.json
        schedule.title = data['title']
        schedule.date = data['date']
        schedule.time = data['time']
        db.session.commit()
        return jsonify({"message": "Schedule updated"}), 200

    elif request.method == 'DELETE':
        db.session.delete(schedule)
        db.session.commit()
        return jsonify({"message": "Schedule deleted"}), 200

@app.route('/quotes', methods=['GET', 'POST'])
def manage_quotes():
    if request.method == 'GET':
        quotes = Quote.query.all()
        return jsonify([{"id": q.id, "text": q.text} for q in quotes]), 200

    elif request.method == 'POST':
        data = request.json
        new_quote = Quote(text=data['text'])
        db.session.add(new_quote)
        db.session.commit()
        return jsonify({"message": "Quote created", "id": new_quote.id}), 201

@app.route('/quotes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_quote(id):
    quote = Quote.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify({"id": quote.id, "text": quote.text}), 200

    elif request.method == 'PUT':
        data = request.json
        quote.text = data['text']
        db.session.commit()
        return jsonify({"message": "Quote updated"}), 200

    elif request.method == 'DELETE':
        db.session.delete(quote)
        db.session.commit()
        return jsonify({"message": "Quote deleted"}), 200
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5003)
