from flask import Flask, render_template, request, redirect, url_for
from participant_class import shuffle, Participant
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'  # SQLite database file

db = SQLAlchemy(app)

app.app_context().push()

class ParticipantModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    assigned_recipient_id = db.Column(db.Integer, db.ForeignKey('participant_model.id'))
    assigned_recipient = db.Column(db.String(10))

db.create_all()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/reveal', methods=['GET', 'POST'])
def reveal():
    participants = []
    all_participants = []

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input:
            new_participant_names = [name.strip() for name in user_input.split(',')]
            participants = [Participant(name) for name in new_participant_names]

            if len(participants) > 1:
                shuffle(participants)
                for participant in participants:
                    participant.assign(participants)

                
                participants_models = []
                for participant in participants:
                    try:
                        participant_model = ParticipantModel.query.filter_by(name=str(participant.name)).one()
                    except NoResultFound:
                        participant_model = ParticipantModel(name=str(participant.name))
                        db.session.add(participant_model)

                    # Assign recipient
                    recipient_name = str(participant.assigned_recipient.name) if participant.assigned_recipient else None
                    recipient_model = ParticipantModel.query.filter_by(name=recipient_name).first()

                    if recipient_model is None:
                        recipient_model = ParticipantModel(name=recipient_name)
                        db.session.add(recipient_model)

                    participant_model.assigned_recipient = str(recipient_model.name)  # Convert to string
                    participants_models.append(participant_model)

                # Commit changes to the database
                db.session.commit()

            all_participants = ParticipantModel.query.all()
            return redirect(url_for('timer'))

    return render_template('reveal.html', participants=all_participants)

@app.route('/timer')
def timer():
    return render_template("timer.html")


@app.route('/not_yet')
def not_yet():
    return render_template('not_yet.html')

@app.route('/reveal2')
def reveal2():
    all_participants = ParticipantModel.query.all()
    return render_template('reveal2.html', participants = all_participants)

@app.route('/reset_database', methods=['POST'])
def reset_database():
    # Code to reset your database (you'll need to implement this based on your database setup)
    # For example, if you're using SQLAlchemy:
    db.drop_all()
    db.create_all()

    # Redirect back to the 'reveal' page after resetting the database
    return redirect(url_for('reveal'))

if __name__ == "__main__":
    app.run(debug=True)

