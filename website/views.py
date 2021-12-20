from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/user-home')
def user_home():
    return render_template('user_home.html')

@views.route('/about')
def about():
    return render_template('about.html')

@views.route('/education')
def education():
    return render_template('education.html')

@views.route('/work')
def work():
    return render_template('work.html')

@views.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/skills')
def skills():
    return render_template('skills.html')