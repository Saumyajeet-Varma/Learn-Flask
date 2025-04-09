from flask import Flask
from side import side
from admin import admin

app = Flask(__name__)
app.register_blueprint(side, url_prefix = "/route/side")
app.register_blueprint(admin, url_prefix = "/admin")

@app.route("/")
@app.route("/home")
def home(): 
    return "<h1>Homepage</h1>"

if __name__ == "__main__":
    app.run(debug = True)