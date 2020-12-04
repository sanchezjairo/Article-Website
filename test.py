import jinja2
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('login.html')