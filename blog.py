from flask import Flask, render_template, session, \
	flash, redirect, url_for, g

import sqlite3

DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'rmrmsadkasdhigfkdfghidfghidfhg'

app = Flask(__name__)

app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE'])

@app.route("/", methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials, Please try agian'
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error = error), status_code

@app.route('/main')
def main():
	return render_template('main.html')

if __name__ == '__main__':
	app.run(debug= True)

