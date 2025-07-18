from app import app
from models import db, Topic, Language

# Sample data
topics = ["Web Development", "Machine Learning", "Cybersecurity", "Blockchain", "AI", "Data Science", "Cloud Computing", "Mobile Development", "Game Development", "DevOps"]
languages = ["Python", "JavaScript", "Java", "C++", "Go", "Ruby", "PHP", "Swift", "Kotlin", "Rust"]

with app.app_context():

    # Add Topics
    for name in topics:
        if not Topic.query.filter_by(name=name).first():
            db.session.add(Topic(name=name))

    # Add Languages
    for name in languages:
        if not Language.query.filter_by(name=name).first():
            db.session.add(Language(name=name))

    db.session.commit()
    print("Seeding completed ✅")
