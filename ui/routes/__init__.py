from flask import Blueprint
from . import main, announcement, requests

Routes = Blueprint('routes', __name__, template_folder='templates')

Routes.add_url_rule(
    '/',
    'announcements',
    view_func=announcement.render_page,
    methods=["GET"]
)

Routes.add_url_rule(
    '/get_count',
    'get_count',
    view_func=announcement.get_announcements,
    methods=["GET"],
)

Routes.add_url_rule(
    '/login',
    'login',
    view_func=login
)