from infrastructure.session_wrapper import SessionWrapper


class DBConn:
    def __init__(self, db: SessionWrapper):
        self.db = db.session

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()
