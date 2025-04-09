from flask import Flask
from admin.main_file import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")

@app.route("/")
def home():
    return "<h1>Homepage</h1>"

if __name__ == "__main__":
    app.run(debug=True)