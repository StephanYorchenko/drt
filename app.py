from flask import Flask
from flask_bootstrap import Bootstrap

from application.user_manager import UserManager
from infrastructure import DBUser
from infrastructure.config import Config
from ui.routes import RouteManager, Authentication
from ui.routes.announcement_provider import AnnouncementProvider


app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

auth_db_worker = UserManager(DBUser())
auth_manager = Authentication(auth_db_worker)
announcement_provider = AnnouncementProvider()
route_manager = RouteManager(auth_manager, announcement_provider)

app.register_blueprint(route_manager.Routes)

if __name__ == '__main__':
	app.run(debug=True, port=8001, host='0.0.0.0')
