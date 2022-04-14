from flask import Flask

app = Flask(__name__)


@app.route('/')
def happy():
    return '<h1>Happy Tamil New Year!</h1>'
