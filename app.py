from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.get("/")
    def main():
        return render_template("index.html")

    return app