import os
from flask import Flask, request, jsonify
from models import db, Quote
from config import Config
from flask_cors import CORS
from sqlalchemy.sql import func

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

# Initializing the database connection
db.init_app(app)

@app.route("/quotes/random", methods=["GET"])
def get_random_quote():
    quote = Quote.query.order_by(func.random()).first()
    if quote:
        return {"quote": quote.text}, 200
    else:
        return {"error": "No quotes available"}, 404


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
    
def seed_data():
    if Quote.query.first() is None:  # Checking to avoid duplicate seeding
        quotes = [
            "Believe you can and you're halfway there.",
            "Your limitation—it's only your imagination.",
            "Push yourself, because no one else is going to do it for you.",
            "Great things never come from comfort zones.",
            "Success doesn’t just find you. You have to go out and get it."
            "The best way to get started is to quit talking and begin doing.",
            "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.",
            "Don't let yesterday take up too much of today.",
            "You learn more from failure than from success. Don't let it stop you. Failure builds character.",
            "It's not whether you get knocked down, it's whether you get up."
        ]
        for text in quotes:
            db.session.add(Quote(text=text))

        db.session.commit()
        print("Database seeded.")    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
        seed_data()
    app.run(host="0.0.0.0", port=5002)
