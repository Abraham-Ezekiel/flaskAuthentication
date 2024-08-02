from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def welcome():
	return ("you are welcome")

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True, port = 5001)
