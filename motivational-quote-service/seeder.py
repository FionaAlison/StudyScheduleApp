from models import db, Quote
from app import app

# List of initial quotes
initial_quotes = [
    "The best way to get started is to quit talking and begin doing.",
    "The pessimist sees difficulty in every opportunity. The optimist sees opportunity in every difficulty.",
    "Don't let yesterday take up too much of today.",
    "You learn more from failure than from success. Don't let it stop you. Failure builds character.",
    "It's not whether you get knocked down, it's whether you get up."
]

with app.app_context():
    db.create_all()
    # Check if the table already has data
    if not Quote.query.first():
        for quote_text in initial_quotes:
            quote = Quote(text=quote_text)
            db.session.add(quote)
        db.session.commit()
        print("Database seeded with initial quotes.")
    else:
        print("Database already contains quotes. Skipping seeding.")
