import jinja2
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)



@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('search'))
    return render_template('login.html', error=error)

@app.route('/article_results')

if __name__ == '__main__':
    app.run(debug=True)