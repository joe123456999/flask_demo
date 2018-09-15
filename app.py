from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/Joe")
def Joe():
    return "Hello Joe!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/add/<int:num1>/<int:num2>')
def show_post(num1, num2):
    # show the post with the given id, the id is an integer
    sum =  num1+num2
    return 'Sum: %d' % sum

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath

if __name__ == "__main__":
    app.run()