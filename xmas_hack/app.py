from flask import Flask, render_template, request, redirect, url_for
from participant_class import shuffle, Participant



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/reveal', methods=['GET', 'POST'])
def reveal():
    participants = []

    if request.method == 'POST':
        user_input = request.form['user_input']

        if user_input:
            new_participant_names = [name.strip() for name in user_input.split(',')]

            for name in new_participant_names:
                new_participant = Participant(name)
                participants.append(new_participant)

            remaining_participants = participants.copy()

            # for x in range(0, len(participants) -1):
            #     participants[x].assign(participants[x+1])
            #     if x == len(participants) -1:
            #         participants[len(participants) -1].assign(participants[0])
            # while len(remaining_participants) >= 1:
            #     for participant in participants:
            #         participant.assign(remaining_participants)
            #         if participant.assigned_recipient in remaining_participants:
            #             remaining_participants.remove(participant.assigned_recipient)

    return render_template('reveal.html', participants=participants)


@app.route('/timer')
def timer():
    return render_template("timer.html")


@app.route('/not_yet')
def not_yet():
    return render_template('not_yet.html')

if __name__ == "__main__":
    app.run(debug=True)

