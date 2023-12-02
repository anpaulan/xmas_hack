from flask import Flask, render_template, request, redirect, url_for
from participant_class import *
from datetime import datetime, timedelta

app = Flask(__name__)
participants = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/reveal')

def reveal():
    ...


if __name__ == '__main__':
    app.run(debug=True)

