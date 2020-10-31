шfrom flask import Blueprint
from . import auth, main, labeling, admin, next_case, task, learning

Routes = Blueprint('routes', __name__,
				   template_folder='templates')

Routes.add_url_rule('/', 'main', view_func=main.main)
