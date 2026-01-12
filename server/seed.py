# server/seed.py
from app import app
from models import db, Message

with app.app_context():
    print("Seeding database...")
    Message.query.delete()

    msg1 = Message(body="Hello, World!", username="Ian")
    msg2 = Message(body="Flask + React = ❤️", username="Ada")
    msg3 = Message(body="Full stack fun time!", username="Lin")

    db.session.add_all([msg1, msg2, msg3])
    db.session.commit()
    print("Seeding complete!")