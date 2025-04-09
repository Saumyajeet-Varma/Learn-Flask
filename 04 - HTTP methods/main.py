from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['name']
        return redirect(url_for("user", usr = user))
    else:
        return render_template("index.html")

@app.route("/user/<usr>")
def user(usr):
    return f"<h1>Hi {usr}!</h1>"

if __name__ == "__main__":
    app.run(debug = True)