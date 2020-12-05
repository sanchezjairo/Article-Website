import jinja2
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/search_results', methods=['GET', 'POST'])
def search_results():
    return render_template('search_results.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    error = None
    if request.method == 'POST':
        if request.form.get('search') != 'article':
            error = 'Please input a keyword or search term'
        else:
            return redirect(url_for('search_results'))
            
    return render_template('search.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'a' or request.form['password'] != 'a':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('search'))

    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)