from flask import Blueprint
from . import main, announcement, requests, auth

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
	'/auth',
	'auth',
	view_func=auth.try_authorize,
	methods=["POST"],
)

Routes.add_url_rule(
	'/check',
	'check',
	view_func=auth.check_auth,
	methods=["POST"],
)

Routes.add_url_rule(
	'/logout',
	'logout',
	view_func=auth.logout,
	methods=["GET"],
)
