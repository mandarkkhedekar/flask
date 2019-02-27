from flask import Flask
app =  Flask (__name__)

@app.route('/hello/<username>')
def hello_name(username):
   return 'Hello %s!' % username



if __name__=='__main__':
    app.run(debug=True)