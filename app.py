from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hier komt de big data applicatie</p>"

