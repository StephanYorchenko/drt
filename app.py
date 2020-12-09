from flask import Flask
from flask_bootstrap import Bootstrap

from application.user_manager import UserManager
from application.desks.desk import Provider
from application.record_transformer.domain_transformer import DomainTransformer
from domain.announcement.announcement import Announcement
from infrastructure import DBUser, DBAnnouncement
from infrastructure.config import Config
from ui.routes import RouteManager, Authentication
from ui.routes.desk_provider import DeskProvider
from ui.routes.user_controller import UserController
from di_container.container import Container, Instantiation


def get_app():
    announcement_transformer = DomainTransformer(
        lambda record: Announcement(
            record.title,
            record.text,
            record.user_id,
            record.date
        )
    )

    container = Container('app')

    container.register_value(announcement_transformer)\
        .to_type(DomainTransformer)

    container.register_value(DBAnnouncement())\
        .to_type(DBAnnouncement)

    container.register_value(DBUser())\
        .to_type(DBUser)

    container.register_type(Provider, Instantiation.Singleton)\
        .to_type(Provider)

    container.register_type(UserManager, Instantiation.Singleton)\
        .to_type(UserManager)

    container.register_type(UserController, Instantiation.Singleton)\
        .to_type(UserController)

    container.register_type(Authentication, Instantiation.Singleton)\
        .to_type(Authentication)

    container.register_type(DeskProvider, Instantiation.Singleton).\
        to_type(DeskProvider)\
        .with_params(name='announcements')

    container.register_type(RouteManager, Instantiation.Singleton)\
        .to_type(RouteManager)

    routes = container.resolve_type(RouteManager)

    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(routes.Routes)

    return app


if __name__ == '__main__':
    app = get_app()
    app.run(debug=True, port=8001, host='0.0.0.0')

