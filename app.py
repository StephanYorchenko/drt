from flask import Flask
from flask_bootstrap import Bootstrap

from infrastructure.config import Config
from ui.routes import Routes as RFront

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

app.register_blueprint(RFront)

if __name__ == '__main__':
	app.run(debug=True, port=8001, host='0.0.0.0')
