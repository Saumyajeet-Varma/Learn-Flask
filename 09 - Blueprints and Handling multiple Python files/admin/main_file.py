from flask import Blueprint

admin = Blueprint("admin", __name__, static_folder="./static", template_folder="./templates")

@admin.route("/")
def admin_page():
    return "<h1>Admin's page</h1>"