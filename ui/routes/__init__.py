from flask import Blueprint

from . import main, announcement_provider, request_provider, auth
from .announcement_provider import AnnouncementProvider
from .auth import Authentication
from .user_controller import UserController


class RouteManager:
    def __init__(
            self,
            authenticator: Authentication,
            announcements: AnnouncementProvider,
            user_control: UserController
    ):
        self.authenticator = authenticator
        self.announcements = announcements
        self.user_control = user_control

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

        self.Routes.add_url_rule(
            '/api/user',
            'user',
            view_func=self.user_control.get_user,
            methods=["GET"]
        )

        self.Routes.add_url_rule(
            '/api/create_user',
            'create_user',
            view_func=self.user_control.add_user,
            methods=["POST"]
        )

        self.Routes.add_url_rule(
            '/api/user_list',
            'user_list',
            view_func=self.user_control.get_all_users,
            methods=["GET"]
        )
