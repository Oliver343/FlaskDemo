from unicodedata import name
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello! This is the main page <h1>HELLO</h1>"


@app.route("/<name>")
def user(name):
    return f"""Hello {name}! \n <marquee behavior="alternate" direction="down" height="600" scrollamount="20" style="border:solid" width="800"> <marquee behavior="alternate"> <p><a href="/">Welcome</a></p> </marquee> </marquee></p> </div> """


if __name__ == "__main__":
    app.run()
