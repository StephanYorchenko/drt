from flask import Blueprint

from . import main, announcement_provider, request_provider, auth
from .announcement_provider import AnnouncementProvider
from .auth import Authentication


class RouteManager:
    def __init__(
            self,
            authenticator: Authentication,
            announcements: AnnouncementProvider
    ):
        self.authenticator = authenticator
        self.announcements = announcements

        self.Routes = Blueprint(
            'routes',
            __name__,
            template_folder='templates'
        )

        self.Routes.add_url_rule(
            '/api/get_count',
            'get_count',
            view_func=self.announcements.get,
            methods=["GET"],
        )

        self.Routes.add_url_rule(
            '/api/auth',
            'auth',
            view_func=self.authenticator.try_authorize,
            methods=["POST"],
        )

        self.Routes.add_url_rule(
            '/api/check',
            'check',
            view_func=self.authenticator.check_auth,
            methods=["POST"],
        )

        self.Routes.add_url_rule(
            '/api/logout',
            'logout',
            view_func=self.authenticator.logout,
            methods=["POST"],
        )
