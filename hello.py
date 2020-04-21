from flask import Flask
from flask import render_template
# -*- coding: utf-8 -*-

from flask import request
from flask_bootstrap import Bootstrap

from forms import bc_form
from logic import get_generation, get_generation_desc, get_side_effects
import pdb

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
bootstrap = Bootstrap(app)

@app.route('/')
def hello_world():
	form = bc_form()
	return render_template('hello.html', form=form)

@app.route('/results', methods=['POST'])
def get_results():
	submitted= request.form['pill_name']
	g_name = get_generation(submitted)
	if g_name:
		testosterone, progestin, adv, disadv, gen_se = get_generation_desc(g_name, submitted)
		if progestin: 
			return render_template('results.html', submitted=submitted, generation=g_name, testosterone=testosterone, progestin=progestin,
								   advantages=adv, disadvantages=disadv, side_effects=gen_se)
	return render_template('no_idea.html', submitted=submitted)

@app.route('/about')
def get_about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run()
