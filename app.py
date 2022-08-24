from flask import Flask

from script import *

def create_app():
    app = Flask(__name__)

    @app.route("/upload", methods=["GET", "POST"])
    def upload_file():
        return upload()

    return app

