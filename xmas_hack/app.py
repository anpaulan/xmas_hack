from flask import Flask, render_template, request, redirect, url_for
from participant_class import shuffle, Participant



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    names = []
    if request.method == 'POST':
        user_input = request.form['user_input']
        if user_input:
           
            new_participant_names = [name.strip() for name in user_input.split(',')]
            
           
            for name in new_participant_names:
                new_participant = Participant(name)
                names.append(new_participant)

                

    if len(names) > 1:
        shuffle(names)
        for participant in names:
            participant.assign(names)
        

    return render_template('reveal.html', participants=names)


@app.route('/reveal')
def reveal():
    return render_template('reveal.html')

@app.route('/timer')
def timer():
    return render_template("timer.html")


if __name__ == "__main__":
    app.run(debug=True)

