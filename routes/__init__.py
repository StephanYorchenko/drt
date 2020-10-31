from flask import Blueprint
from . import main

Routes = Blueprint('routes', __name__,
				   template_folder='templates')

Routes.add_url_rule('/', 'main', view_func=main.main)
