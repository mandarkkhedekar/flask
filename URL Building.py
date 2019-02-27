from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guests/<name>')
def guests(name):
    return 'Hello %s as Guest' %name

@app.route('/user/<username>')
def hello_user(username):
    if username == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('guests', name=username))

if __name__ == '__main__' :
     app.run(debug=True)