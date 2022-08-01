from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
 "apiKey": "AIzaSyCGCHysCQs_oHGc3rQ2MCJ82vbsr3eBYVo",
  "authDomain": "fir-160ae.firebaseapp.com",
  "databaseURL": "https://fir-160ae-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "fir-160ae",
  "storageBucket": "fir-160ae.appspot.com",
  "messagingSenderId": "531779820040",
  "appId": "1:531779820040:web:3326b20b3c332e38c54fbd",
  "measurementId": "G-Z33RMDTMYB",
  "databaseURL" : ""
  }
firebase = pyrebase.initialize_app (config)
auth = firebase.auth()
#db= firebase.database()



app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('add_tweet'))
		except:
			error = "Authentication failed"

	return render_template("signin.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.create_user_with_email_and_password(email, password)
			return redirect(url_for('add_tweet'))
		except:
			error = "Authentication failed"
			return error
	else:
		return render_template("signup.html")


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
	return render_template("add_tweet.html")


if __name__ == '__main__':
	app.run(debug=True)