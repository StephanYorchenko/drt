from flask import Flask
from flask_bootstrap import Bootstrap

from application.authenticator import Authenticator
from infrastructure import DBUser
from infrastructure.config import Config
from ui.routes import RouteManager, Authentication


app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

auth_db_worker = Authenticator(DBUser())
auth_manager = Authentication(auth_db_worker)
route_manager = RouteManager(auth_manager)

app.register_blueprint(route_manager.Routes)

if __name__ == '__main__':
	app.run(debug=True, port=8001, host='0.0.0.0')
