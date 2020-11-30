from flask import Blueprint, send_from_directory
from . import main, announcement, requests, auth

Routes = Blueprint('routes', __name__, template_folder='templates')


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
		methods=["POST"],
)
