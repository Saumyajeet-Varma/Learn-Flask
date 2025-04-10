# Learn Flask



## Table of Contents
- [Getting Started](#getting-started)
- [How to make a Website with Python](#01-how-to-make-a-website-with-python)
- [HTML Templates](#02-html-templates)
- [Template Inheritance](#03-template-inheritance)
- [HTTP Methods](#04-http-methods)
- [Session](#05-session)
- [Message Flashing](#06-message-flashing)
- [Using SQLAlchemy Database](#07-using-sqlalchemy-database)
- [Handling Static Files](#08-handling-static-files)
- [Blueprints and handling multiple python files](#09-blueprints-and-handling-multiple-python-files)



## Getting Started

Flask is a micro web framework written in Python. It's used to build web applications quickly and with minimal code.

- Routing: Define URLs and what happens when someone visits them.
- Templating: Uses Jinja2 templating engine to render HTML dynamically.
- Built-in development server & debugger.
- RESTful request handling.
- Easily extendable with plugins (e.g., for databases, authentication, etc.).

### Install Flask
```bash
pip install flask
```

### Basic code snippet to create a server using flask
```python
from flask import Flask

app = Flask(__name__)


# Models and routes


if __name__ == "__main__":
    app.run()
```

Visit [localhost:5000](http://localhost:5000) in your browser.

You need to restart the server manually for every change to display it in webpage. If you want the server to detect the change and restart itself, you can use a parameter **debug** in **run**.
```python
app.run(debug=True)
```



## 01) How to make a website with Python

In this section we'll learn how to create **routes** and **redirection**.

### Routing
```python
@app.route("/")
def home():
    return "<h1>This is the Homepage</h1>"
```
You're telling Flask:
> "Hey Flask, when someone visits the root URL /, run the home() function and return whatever it outputs as the response."

```python
@app.route("/user/<name>")  # Dynamic routing
def user(name):
    return f"Hello {name}"
```
> <variable_name> is used in dynamic routing in Flask

### Redirection
For redirection you need to import redirect and url_for from flask.
```python
from flask import redirect, url_for
```

```python
@app.route("/test")
def test():
    return redirect(url_for("home"))
```

```python
@app.route("/another-test")
def test():
    return redirect(url_for("user", name = "Samm"))  # Redirection to dynamic routes
```



## 02) HTML templates

In this section we'll learn how to render proper **HTML template**.

Create a directory in the root folder where your **main.py** is, name that directory **templates**. Inside templates create your HTML files.

Jinja (specifically Jinja2) is the template engine that Flask uses under the hood. <br>
Jinja’s main job is to dynamically generate HTML by embedding Python-like expressions inside your HTML files.

To render HTML pages, we need **render_template**
```python
from flask import render_template
```

How to use render_template
```python
@app.route("/")
def home():
    return render_template("index.html")
```
You're telling Flask:
> "Hey Flask, when someone visits the root URL /, run the home() function, and send back the rendered HTML content from the index.html file inside the templates folder as the response."

We can also pass template variables
```python
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name = name, role = "admin", x = 10)
```
> We can pass any datatype as template variables.

How to use template variable in HTML
```html
<h1>Hello {{name}}</h1>
<h4>You are {{role}}</h4>
```

```html
{% for i in range(x) %} 
    {% if i % 2 == 0 %}
        <p>{{i}}</p>
    {% endif %}
{% endfor %}
```
> {{ }} is used to show the value. <br> {% %} is used to write python code.



## 03) Template inheritance

In this section we'll learn the concept of **Template inheritance**.

Template inheritance in Flask (via Jinja2) allows you to create a base HTML structure that other templates can extend. This promotes reusability and consistency across your web pages.

### Basic Structure
1. Create a base template
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>
    
    <main>
        {% block content %}
        <!-- Child templates inject content here -->
        {% endblock %}
    </main>

    <footer>
        <p>&copy; 2025</p>
    </footer>
</body>
</html>
```

2. Extend the base in a child template
```html
<!-- templates/home.html -->
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <p>This is the home page content.</p>
{% endblock %}
```

### How it works
> {% extends "base.html" %} tells Jinja to use the layout from base.html. <br> {% block %} tags in the base file are placeholders that the child templates fill in. <br> {% block block_name %}  a block name is an identifier you define inside the {% block ... %} tag. It's like a placeholder section in your base template that child templates can override or fill in.



## 04) HTTP methods

In this section we'll learn about **HTTP methods** in Flask.

HTTP methods determine the type of request the client sends to the server.

### Common HTTP Methods
| Method | Use Case |
|--------|----------|
| GET    | Retrieve data from the server |
| POST   | Submit data to the server |
| PUT    | Update existing data |
| DELETE | Delete data from the server |
| PATCH  | Partially update data |

Import request from flask to access the data sent by the client.
```python
from flask import request
```


### Flask Example with GET and POST
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return '''
        <form method="post">
            <input type="text" name="name" placeholder="Enter your name">
            <input type="submit">
        </form>
    '''
```
> GET shows the form. <br> POST handles the form submission and greets the user.



## 05) Session

In this section we'll learn about **session** in Flask

In Flask, a session is used to store information across requests for a single user—like login status, user preferences, or shopping cart items. <br>
It’s basically a temporary storage mechanism that persists between different pages/views for the same user.

###  Setup: Set the secret key
```python
from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # needed to use sessions
```

### Example: Using session to store login info
```python
from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def home():
    if 'username' in session:
        return f"Welcome back, {session['username']}!"
    return "You are not logged in. <a href='/login'>Login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return '''
        <form method="post">
            <input type="text" name="username" placeholder="Enter name">
            <input type="submit">
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))
```

### Useful Session Operations
| Operation                         | Description                            |
|----------------------------------|----------------------------------------|
| `session['key'] = value`         | Set a session value                    |
| `session.get('key')`             | Get a session value                    |
| `session.pop('key', None)`       | Remove a specific key from the session |
| `session.clear()`                | Clear the entire session               |
> session stores data in dictionary (key-value pair).

### Permanent Session
By default, Flask sessions last only until the browser is closed (they are temporary). <br>
If you want a session to persist even after closing the browser, you can make it permanent.

You just need to set:
```python
session.permanent = True
```
> You can also set the duration for how long the session should last. By default it is 31 days

##### Example
```python
from flask import Flask, session, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Set session lifetime (optional)
app.permanent_session_lifetime = timedelta(days=7)

@app.route('/login')
def login():
    session.permanent = True  # Mark this session as permanent
    session['user'] = 'Alice'
    return 'Logged in with a permanent session!'

@app.route('/get')
def get():
    user = session.get('user')
    return f'Hello, {user}' if user else 'No user logged in.'
```



## 06) Message flashing

In this section we'll learn about **Message Flashing** in Flask.

Flashing is a way to send a message to the next request, usually used to display status messages like:
- ✅ “You have successfully logged in.”
- ❌ “Invalid password.”
- ⚠️ “Please fill all required fields.”

### Example
```python
from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # required for flashing

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        if user == 'admin':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username!', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')
```
> *flash(message)* - 	Stores a message for the next view

###  In Your Template (home.html, login.html, etc.):
```python
{% with messages = get_flashed_messages(with_categories=true) %}
  {% if messages %}
    <ul>
    {% for category, message in messages %}
      <li class="{{ category }}">{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}
```

> *get_flashed_messages()* - Retrieves and clears flashed messages

### Flash Message Categories (Optional but useful!)
| Category   | Purpose                     | Example Usage                            |
|------------|-----------------------------|-------------------------------------------|
| `success`  | For positive feedback        | `flash("Logged in successfully!", "success")` |
| `error`    | For error messages           | `flash("Invalid password!", "error")`        |
| `warning`  | For caution or alerts        | `flash("Your session is about to expire.", "warning")` |
| `info`     | For general information      | `flash("New feature launched!", "info")`     |

##### Used like this:
```python
flash("Something went wrong!", "error")
```



## 07) Using SQLAlchemy Database

In this section we'll learn how to integrate **SQLAchemy** with Flask.

To integrate **SQLAchemy**, we need to install **Flask-SQlAlchemy**
```bash
pip install flask-sqlalchemy
```

### Basic setup
```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'  # or PostgreSQL/MySQL URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

### Defining a model
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'
```
> column_name = db.Column(column_datatype, ...optional_arguements) <br>
> `__init__`: You can define an `__init__` method, but you don't need to if you're just assigning attributes that match the model fields. SQLAlchemy auto-generates a default constructor unless you want custom behavior. <br>
> `__repr__`: Defines how the object is represented as a string (for debugging/logs).

### Creating a database
```python
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Creates tables based on the models
    app.run()
```

### CRUD Example
```python
# CREATE
new_user = User(username='john', email='john@example.com')
db.session.add(new_user)
db.session.commit()

# READ
user = User.query.filter_by(username='john').first()

# UPDATE
user.email = 'john.doe@example.com'
db.session.commit()

# DELETE
db.session.delete(user)
db.session.commit()
```



## 08) Handling static files

In this section we'll learn how to handle **static files** in Flask.

We create a separate folder for static files and name it "static":

```md
your_project/
│
├── main.py
├── static/
│   ├── styles/
│   │   └── style.css
│   ├── scripts/
│   │   └── script.js
│   └── images/
│       └── logo.png
│
├── templates/
│   └── index.html
```

Now how to access the static files
```html
<!-- CSS files -->
<link rel="stylesheet" href="{{ url_for('static', filename='styles/style.css') }}">
```

```html
<!-- JavaScript files -->
<script src="{{ url_for('static', filename='scripts/script.js') }}"></script>
```

```html
 <!-- Images -->
<img src="{{ url_for('static', filename='images/logo.png') }}" alt="Logo">
```



## 09) Blueprints and Handling multiple Python files

In this section we'll learn about **Blueprints** in Flask.

**Flask Blueprints** are a powerful way to organize your application into modular components, especially helpful as your app grows. Think of blueprints like “mini-apps” that can be plugged into the main Flask app.

### Why Use Blueprints ?
- Cleaner, modular code
- Separate concerns (routes, templates, static files)
- Easy to reuse and scale

### Example Folder Structure with Blueprints
```md
your_project/
│
├── main.py
├── static/
├── templates/
│
├── admin/
│   ├── admin.py
│   ├── static/
│   └── templates/
```

### Step-by-Step Guide

#### 1. admin/admin.py — Define a Blueprint
```python
from flask import Blueprint, render_template

admin = Blueprint("admin", __name__, static_folder="static", template_folder="templates")

@admin.route('/')
def admin_page():
    return render_template('admin_page.html')

```
> Blueprint("blueprint_name", `__name__`, static_folder="path_to_static_folder", template_folder="patgh_to_template_folder")

#### 2. main.py — Register the Blueprint
```python
from flask import Flask
from admin.admin import admin

app = Flask(__name__)
app.register_blueprint(admin, url_prefix="/admin")

if __name__ == '__main__':
    app.run(debug=True)
```
> register_blueprint("blueprint_name", url_prefix="/prefix_route") <br> *url_prefix is optional*

> For better clarity checkout the code given in the [09 - Blueprints and Handling multiple Python files](https://github.com/Saumyajeet-Varma/Learn-Flask/tree/main/09%20-%20Blueprints%20and%20Handling%20multiple%20Python%20files)