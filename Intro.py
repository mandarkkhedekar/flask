from flask import Flask
app =  Flask (__name__)

@app.route('/')
def hello():
    return 'Hello Flask! This is just an intro'


@app.route('/tuna')
def tuna():
    return('<h1>I love Tuna</h1>')

@app.route('/profile/<username>')
def profile(username):
    return "Hello %s" %username


@app.route('/post/<int:post_id>')
def posts(post_id):
    return "Hello %s" %post_id


if __name__=='__main__':
    app.run(debug=True)