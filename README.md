# Learn Flask

## Table of Contents
- [Getting Started](#getting-started)
- [How to make a website with Python](#01-how-to-make-a-website-with-python)
- [HTML Templates](#02-html-templates)



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

Visit [localhost:5000](http://127.0.0.1:5000) in your browser.

You need to restart the server manually for every change to display it in webpage. If you want the server to detect the change and restart itself, you can use a parameter **debug** in **run**.
```python
app.run(debug=True)
```



## 01) How to make a website with Python

In this section we'll learn how to create routes and redirection.

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

In this section we'll learn how to render proper HTML template

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
