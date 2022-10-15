import os
from notesapp.config import app_config
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(app_config[os.environ['FLASK_DEBUG']])

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/auth/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 5000))
    app.run('0.0.0.0', PORT)