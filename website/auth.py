from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def sign_up():
    return "<p>Sign Up</p>"

@auth.route('/signin')
def signin():
    return "<p>Sign In</p>"

@auth.route('/signout')
def signout():
    return "<p>Sign Out</p>"

