from flask import render_template, session
from flask_login import login_required

from infrastructure import DBUser

def main():
    return render_template('base.html')
