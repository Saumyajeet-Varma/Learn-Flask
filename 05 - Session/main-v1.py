from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "secretkeyforsession"

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form['name']
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("index.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>Hi {user}!</h1>"
    else:
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug = True)