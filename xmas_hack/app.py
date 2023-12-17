from flask import Flask, render_template, request, redirect, url_for
from participant_class import shuffle, Participant
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from flask import jsonify

app = Flask(__name__)
# Created the SQLite database.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SECRET_KEY'] = 'key8742938472'
db = SQLAlchemy(app)

app.app_context().push()

class ParticipantModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    assigned_recipient_id = db.Column(db.Integer, db.ForeignKey('participant_model.id'))
    assigned_recipient = db.Column(db.String(10))

db.create_all()

class ParticipantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    assigned_recipient_id = IntegerField('Assigned Recipient ID')
    assigned_recipient = StringField('Assigned Recipient')
 

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/reveal', methods=['GET', 'POST'])
def reveal():
    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input:
            new_participant_names = [name.strip() for name in user_input.split(',')]

            for name in new_participant_names:
                participant_model = ParticipantModel(name=name)
                db.session.add(participant_model)

            db.session.commit()

            return redirect(url_for('reveal_list'))

    return render_template('reveal.html')

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

    db.drop_all()
    db.create_all()

    return redirect(url_for('reveal'))

@app.route('/edit', methods=['GET', 'POST'])
def edit_participants():
    participants = ParticipantModel.query.all()
    add_form = ParticipantForm()

    if add_form.validate_on_submit():
        new_participant = ParticipantModel(
            name=add_form.name.data,
            assigned_recipient_id=add_form.assigned_recipient_id.data,
            assigned_recipient=add_form.assigned_recipient.data
        )
        db.session.add(new_participant)
        db.session.commit()
        return redirect(url_for('edit_participants'))

    return render_template('edit.html', participants=participants, add_form=add_form)

@app.route('/delete/<int:participant_id>', methods=['GET', 'POST'])
def delete_participant(participant_id):
    participant = ParticipantModel.query.get_or_404(participant_id)

    db.session.delete(participant)
    db.session.commit()
    return redirect(url_for('edit_participants'))

@app.route('/add', methods=['GET', 'POST'])
def add_participant():
    form = ParticipantForm()

    if form.validate_on_submit():
        new_participant = ParticipantModel(
            name=form.name.data
        )
        db.session.add(new_participant)
        db.session.commit()
        return redirect(url_for('edit_participants'))

    return render_template('add.html', form=form)

@app.route('/reveal_list')
def reveal_list():
  
    participants = ParticipantModel.query.all()
    participant_names = [participant.name for participant in participants]

    participants_str = ','.join(participant_names)
   
    db.drop_all()
    db.create_all()

    return redirect(url_for('randomize', participant_names=participants_str))

@app.route('/randomize')
def randomize():

    participant_names = request.args.get('participant_names')
    participants = participant_names.split(",")
    participants = [Participant(name) for name in participants]

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

            recipient_name = str(participant.assigned_recipient.name) if participant.assigned_recipient else None
            recipient_model = ParticipantModel.query.filter_by(name=recipient_name).first()

            if recipient_model is None:
                recipient_model = ParticipantModel(name=recipient_name)
                db.session.add(recipient_model)

            participant_model.assigned_recipient = str(recipient_model.name)
            participants_models.append(participant_model)

        db.session.commit()

    return redirect(url_for('home'))
#
if __name__ == "__main__":
    app.run(debug=True)
