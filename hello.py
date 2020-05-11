from flask import Flask
from flask import render_template
# -*- coding: utf-8 -*-

from flask import request
from flask_bootstrap import Bootstrap

from forms import bc_form, feedback_form, email_form
from logic import get_generation, get_generation_desc, get_side_effects
import pyrebase
import pdb
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
bootstrap = Bootstrap(app)

config = {
    'apiKey': "AIzaSyAsqFbIbpVA-B7_Irqyr4wtNqhNyVtL_js",
    'authDomain': "whatgismybc-4c67a.firebaseapp.com",
    'databaseURL': "https://whatgismybc-4c67a.firebaseio.com",
    'projectId': "whatgismybc-4c67a",
    'storageBucket': "whatgismybc-4c67a.appspot.com",
    'messagingSenderId': "227599748008",
    'appId': "1:227599748008:web:22248703e7d256112cab9d",
    'measurementId': "G-4Y5BQBXC6E"
  };

firebase = pyrebase.initialize_app(config)
db = firebase.database()



@app.route('/')
def hello_world():
	form = bc_form()
	return render_template('hello.html', form=form)

@app.route('/results', methods=['POST'])
def get_results():
	submitted= request.form['pill_name']
	feedback = feedback_form()
	g_name = get_generation(submitted)
	if g_name:
		testosterone, progestin, adv, disadv, gen_se = get_generation_desc(g_name, submitted)
		if progestin: 
			return render_template('results.html', submitted=submitted, generation=g_name, testosterone=testosterone, progestin=progestin,
								   advantages=adv, disadvantages=disadv, side_effects=gen_se, form=feedback)
	return render_template('no_idea.html', submitted=submitted)

@app.route('/results_thank_you', methods=['POST'])
def get_results_thank_you():
	feedback = dict(request.form)
	db.child('feedback').push(feedback)

	email = email_form()
	return render_template('thank_you.html', form=email, formdone=False)

@app.route('/write_email', methods=['POST'])
def get_results_thank_you_email():
	email = dict(request.form)
	db.child('emails').push(email)

	email = email_form()
	return render_template('thank_you.html', form=email, formdone=True)

@app.route('/about')
def get_about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run()
