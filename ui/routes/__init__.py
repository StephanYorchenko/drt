from flask import Blueprint, send_from_directory
from . import main, announcement, requests, auth

Routes = Blueprint('routes', __name__, template_folder='templates')

Routes.add_url_rule(
		'/',
		'main',
		view_func=lambda: send_from_directory('static/dist', 'index.html')
)

Routes.add_url_rule(
		'/dist/<path:path>',
		'static',
		view_func=lambda path: send_from_directory('static/dist', path)
)

Routes.add_url_rule(
		'/api/get_count',
		'get_count',
		view_func=announcement.get_announcements,
		methods=["GET"],
)

Routes.add_url_rule(
		'/api/auth',
		'auth',
		view_func=auth.try_authorize,
		methods=["POST"],
)

Routes.add_url_rule(
		'/api/check',
		'check',
		view_func=auth.check_auth,
		methods=["POST"],
)

Routes.add_url_rule(
		'/api/logout',
		'logout',
		view_func=auth.logout,
		methods=["GET"],
)
