from sqlalchemy.orm import sessionmaker

from infrastructure.engine_wrapper import EngineWrapper


class SessionWrapper:
    def __init__(self, engine: EngineWrapper):
        self.session = sessionmaker(bind=engine.engine, autocommit=True)()
