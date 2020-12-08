from flask import Flask
from flask_bootstrap import Bootstrap

from application import DomainTransformer, Provider, UserManager
from domain import Announcement, Request, HostessRequestType
from infrastructure import DBUser, DBAnnouncement, DBRequest
from infrastructure.config import Config
from ui.routes import RouteManager, Authentication
from ui.routes.desk import Desk
from ui.routes.user_controller import UserController

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

announcement_transformer = DomainTransformer(
    lambda record: Announcement(record.title, record.text,
                                record.user_id, record.date))
announcement_provider = Provider(DBAnnouncement, announcement_transformer, 7)
announcement_desk = Desk(announcement_provider, 'announcements')

request_transformer = DomainTransformer(lambda record:
                                        Request(record.id, HostessRequestType(
                                           record.topic),
                                               record.comment, record.user_id,
                                               record.is_watched))
request_provider = Provider(DBRequest, request_transformer, 7)
request_desk = Desk(request_provider, 'requests')

auth_db_worker = UserManager(DBUser())
user_control = UserController(auth_db_worker)
auth_manager = Authentication(auth_db_worker)
route_manager = RouteManager(auth_manager, announcement_desk,
                             request_desk, user_control)

app.register_blueprint(route_manager.Routes)

if __name__ == '__main__':
    app.run(debug=True, port=8001, host='0.0.0.0')
