from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name, role = "user", age = 21)

@app.route("/python")
def code():
    return render_template("code.html", x = 10)

if __name__ == "__main__":
    app.run()