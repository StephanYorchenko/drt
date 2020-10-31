from flask import Blueprint
from . import main, announcement


Routes = Blueprint('routes', __name__,
				   template_folder='templates')

Routes.add_url_rule('/', 'main', view_func=main.main)
Routes.add_url_rule(
	'/page',
	'get_count',
	view_func=announcement.get_announcements)
