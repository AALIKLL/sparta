from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html", subject="안녕하세요.")


@app.route("/hello/")
def hello():
    return "Hello Flask!"


if __name__ == "__main__":
    app.run()
