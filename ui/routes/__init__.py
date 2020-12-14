from flask import Blueprint

from . import main, auth
from ui.desks import AnnouncementDesk, RequestDesk
from .auth import Authentication
from .user_controller import UserController


class RouteManager:
    def __init__(
            self,
            authenticator: Authentication,
            announcements: AnnouncementDesk,
            requests: RequestDesk,
            user_control: UserController
    ):
        self.authenticator = authenticator
        self.announcements = announcements
        self.user_control = user_control
        self.requests = requests

        self.Routes = Blueprint(
            'routes',
            __name__,
            template_folder='templates'
        )

        self.Routes.add_url_rule(
            '/api/announcement',
            'get_announcement',
            view_func=self.announcements.get,
            methods=["GET"],
        )

        self.Routes.add_url_rule(
            '/api/announcement',
            'post_announcement',
            view_func=self.announcements.add,
            methods=["POST"],
        )

        self.Routes.add_url_rule(
            '/api/requests',
            'get requests',
            view_func=self.requests.get,
            methods=['GET']
        )

        self.Routes.add_url_rule(
            '/api/auth',
            'auth',
            view_func=self.authenticator.try_authorize,
            methods=["POST"],
        )

        self.Routes.add_url_rule(
            '/api/auth/check',
            'check_auth',
            view_func=self.authenticator.check_auth,
            methods=["POST"],
        )

        self.Routes.add_url_rule(
            '/api/user/logout',
            'logout user',
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
            '/api/user',
            'create_user',
            view_func=self.user_control.add_user,
            methods=["POST"]
        )

        self.Routes.add_url_rule(
            '/api/user/list',
            'user_list',
            view_func=self.user_control.get_all_users,
            methods=["GET"]
        )

        self.Routes.add_url_rule(
            '/api/request',
            'get_request',
            view_func=self.requests.get,
            methods=["GET"]
        )

        self.Routes.add_url_rule(
            '/api/request',
            'add_request',
            view_func=self.requests.add,
            methods=["POST"]
        )

        self.Routes.add_url_rule(
            '/api/request',
            'update_request',
            view_func=self.requests.change_approval,
            methods=["PUT"]
        )
