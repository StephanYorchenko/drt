from flask import Blueprint
from . import main, announcement, requests

Routes = Blueprint('routes', __name__,
                   template_folder='templates')

Routes.add_url_rule('/', 'main', view_func=main.main)

Routes.add_url_rule(
    '/announcement',
    'get_count',
    view_func=announcement.get_announcements)

Routes.add_url_rule('/requests',
                    'requests',
                    view_func=requests.get_announcements)
