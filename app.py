from flask import Flask

app = Flask(__name__)


@app.route('/')
def happy():
    return '<h1>Happy Tamil New Year</h1>'
    return '<h2>Aji</h2>'
    return '<h3>Chitra</h3>'
    return '<h3>Divya</h4>'
    return '<h5>Enjoy your day folks!!!</h5>'
