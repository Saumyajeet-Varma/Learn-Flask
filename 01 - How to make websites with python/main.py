from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world, This is main page <h1>HOMEPAGE</h1>"

@app.route("/user/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("home"))

@app.route("/premium-user")
def premium():
    return redirect(url_for("user", name = "Samm"))

if __name__ == "__main__":
    app.run()