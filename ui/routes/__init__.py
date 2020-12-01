from flask import Blueprint

from . import main, announcement, requests, auth
from .auth import Authentication


class RouteManager:
    def __init__(self, authenticator: Authentication):
        self.authenticator = authenticator

        self.Routes = Routes = Blueprint(
            'routes',
            __name__,
            template_folder='templates'
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
            view_func=self.authenticator.try_authorize,
            methods=["POST"],
        )

        Routes.add_url_rule(
            '/api/check',
            'check',
            view_func=self.authenticator.check_auth,
            methods=["POST"],
        )

        Routes.add_url_rule(
            '/api/logout',
            'logout',
            view_func=self.authenticator.logout,
            methods=["POST"],
        )
