from app import db, Quote

def seed_data():
    quotes = [
        "Believe you can and you're halfway there.",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Success doesn’t just find you. You have to go out and get it."
    ]

    for text in quotes:
        db.session.add(Quote(text=text))

    db.session.commit()
    print("Seed data added.")

if __name__ == "__main__":
    with db.app.app_context():
        seed_data()
