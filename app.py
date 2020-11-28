from flask import Flask
from flask_login import LoginManager

from infrastructure.config import Config
from infrastructure import DBUser
from ui.routes import Routes as RFront
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'routes.login'
login.login_message = ':('


@login.user_loader
def load_user(id):
	user = DBUser.get_user(id=int(id))
	return user


bootstrap = Bootstrap(app)

app.register_blueprint(RFront)

if __name__ == '__main__':
	app.run(debug=True, port=8001, host='0.0.0.0')