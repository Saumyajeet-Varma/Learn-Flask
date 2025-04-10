# Learn Flask

## Table of Contents
- [Getting Started](#getting-started)
- [How to make a Website with Python](#01-how-to-make-a-website-with-python)
- [HTML Templates](#02-html-templates)
- [Template Inheritance](#03-template-inheritance)
- [HTTP Methods](#04-http-methods)



## Getting Started

Flask is a micro web framework written in Python. It's used to build web applications quickly and with minimal code.

- Routing: Define URLs and what happens when someone visits them.
- Templating: Uses Jinja2 templating engine to render HTML dynamically.
- Built-in development server & debugger.
- RESTful request handling.
- Easily extendable with plugins (e.g., for databases, authentication, etc.).


### Basic code snippet to create a server using flask

```python
from flask import Flask

app = Flask(__name__)


"""
================= 
Models and routes
================= 
"""

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
@app.route("/user/<name>")    # Dynamic routing
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
    return redirect(url_for("user", name = "Samm"))    # Redirection to dynamic routes
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
