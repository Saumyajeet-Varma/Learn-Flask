from flask import Blueprint

side = Blueprint("side", __name__, static_folder="./static", template_folder="./templates")

@side.route("/")
def side_page():
    return "<h1>Sidepage</h1>"

@side.route("/check")
def check():
    return "<h1>Okay 👍</h1>"