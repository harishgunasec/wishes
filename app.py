from flask import Flask

app = Flask(__name__)


@app.route('/')
def happy():
    return '<h1>Happy Tamil New Year</h1>'
            '<h2>Aji</h2>'
             '<h3>Chitra</h3>'
              '<h3>Divya</h4>'
               '<h5>Enjoy your day folks!!!</h5>'