from sqlalchemy import create_engine

from infrastructure.config import Config


class EngineWrapper:
    def __init__(self):
        self.engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
