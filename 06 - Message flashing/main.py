from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "secretkeyforsession"
app.permanent_session_lifetime = timedelta(days = 7)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form['name']
        session["user"] = user
        flash("Login successfully", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in", "info")
            return redirect(url_for("user"))
        
        return render_template("index.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user = user)
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    user = session["user"]
    flash(f"You've been logged out successfully, {user} !", "info")
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)