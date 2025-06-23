from flask import Blueprint, render_template,request  # type: ignore
from models import Language, Topic, Member,db # type: ignore
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'], defaults={'member_id': None})
@main.route('/<int:member_id>', methods=['GET', 'POST'])
def index(member_id):

    if member_id:
        # Fetch member details if member_id is provided
        member = Member.query.get(member_id)
        if not member:
            return "Member not found", 404
        # Render the form with existing member data
        return render_template('index.html', member=member)
    
    if request.method == 'POST':
        #Gather Data from the form
        email = request.form.get('email')
        password = request.form.get('password')      
        location = request.form.get('location')
        first_learn_date = request.form.get('first_learn_date')
        fav_language = request.form.get('fav_language')
        about = request.form.get('about')
        learn_new_interests = request.form.get('learn_new_interests') == 'on'
        interest_in_topics = request.form.getlist('interest_in_topics')

        # Create a new Member instance
        new_member = Member(
            email=email,
            password=password,
            location=location,
            first_learn_date=datetime.strptime(first_learn_date, '%Y-%m-%dT%H:%M'),
            fav_language=fav_language,
            about=about,
            learn_new_interests=learn_new_interests
        )
        db.session.add(new_member)

        for topic_id in interest_in_topics:
            topic = Topic.query.get(topic_id)
            if topic:
                new_member.interest_in_topics.append(topic)

        db.session.commit()
        return "Form submitted successfully!"
    Languages = Language.query.all()
    Topics = Topic.query.all()
    context = {
        'languages': Languages,
        'topics': Topics,
        'member': member,
        'member_id': member_id
    }
    return render_template('index.html', **context)
