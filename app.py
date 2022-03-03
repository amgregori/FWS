from flask import Flask, render_template

#Create Flask Instance
app = Flask(__name__)


# Create Routes
@app.route('/')
def index():
	first_name = 'Andy'
	favorite_pizza = ['Pepperoni', 'Cheese', 'Onion', "Riccotta"]
	stuff = "This is <strong>BOLD</strong> text"
	return render_template('play.html', first_name=first_name,
		stuff=stuff, pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
	return render_template('user.html', username=name)


# Create Custom Error Pages

#1. Invalid URL:

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#2. Internal Server Error:
@app.errorhandler(500)
def page_not_found(e):
	return render_template('500.html'), 500