from flask import Blueprint
from . import main, announcement, requests

Routes = Blueprint('routes', __name__, template_folder='templates')

Routes.add_url_rule('/', 'main', view_func=main.main)

Routes.add_url_rule(
    '/get_count',
    'get_count',
    view_func=announcement.get_announcements,
    methods=["GET"]
)

Routes.add_url_rule(
    '/anouncements',
    'announcements',
    view_func=announcement.render_page
)
