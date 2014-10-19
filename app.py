from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, welcome to Dboy's Forum!"


if __name__ == "__main__":
    app.run(port = 8889)
