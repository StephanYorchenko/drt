from datetime import datetime

from di_container.container import Container, Instantiation
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from ui import (
    AnnouncementDesk,
    RequestDesk,
    RouteManager,
    Authentication,
    AnnouncementJsonTransformer,
    RequestJsonTransformer,
    JsonTransformer,
    TableRequestJsonTransformer,
    TableRequestDesk

)
from ui.routes.user_controller import UserController

from application import (
    AnnouncementProvider,
    RequestProvider,
    TableRequestProvider,
    TableRequestRecordTransformer,
    RecordTransformer,
    AnnouncementRecordTransformer,
    RequestRecordTransformer,
    UserRecordTransformer,
    Filter,
    AnnouncementFilter,
    RequestFilter,
    TableRequestFilter,
    UserManager
)

from domain import (
    Announcement,
    Request,
    User,
    Role,
    TableRequest
)

from infrastructure import (
    DBUser,
    DBAnnouncement,
    DBRequest,
    AnnouncementRecord,
    RequestRecord,
    UserRecord,
    DBTableRequest,
    TableRequestRecord
)

from infrastructure.config import Config
from infrastructure.database_manager.dblink import DBConn


def get_app():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    session = sessionmaker(bind=engine, autocommit=True)()

    conn_container = Container('dbconn')
    conn_container.register_value(session) \
        .to_type(Session)
    conn_container.register_type(DBConn, Instantiation.Singleton) \
        .to_type(DBConn)

    dbconn = conn_container.resolve_type(DBConn)

    container = Container('app')

    # for user
    container.register_value(RecordTransformer(
        lambda record: User(record.id, record.name, record.password,
                            Role(record.role)),
        lambda user: UserRecord(user.user_id, user.username, user.password,
                                '', int(user.role)))) \
        .to_type(UserRecordTransformer)

    # for announcements
    container.register_value(RecordTransformer(
        lambda record: Announcement(
            record.title,
            record.text,
            record.date),
        lambda announcement: AnnouncementRecord(
            announcement.title,
            announcement.text,
            announcement.date))
    ).to_type(AnnouncementRecordTransformer)
    container.register_value(JsonTransformer(
        lambda json: Announcement(
            json['title'],
            json['text'],
            str(datetime.now().date())))).to_type(AnnouncementJsonTransformer)
    container.register_value(Filter(lambda x: True)) \
        .to_type(AnnouncementFilter)
    container.register_value(DBAnnouncement(dbconn, engine)) \
        .to_type(DBAnnouncement)
    container.register_type(AnnouncementDesk, Instantiation.Singleton). \
        to_type(AnnouncementDesk) \
        .with_params(name='announcements')
    container.register_type(AnnouncementProvider, Instantiation.Singleton). \
        to_type(AnnouncementProvider)

    # for requests
    container.register_value(RecordTransformer(
        lambda record: Request(record.id, record.topic, record.comment,
                               record.username, record.date, record.approved),
        lambda request: RequestRecord(request.id, request.topic,
                                      request.comment, request.username,
                                      request.date, request.approved))) \
        .to_type(RequestRecordTransformer)
    container.register_value(JsonTransformer(
        lambda json: Request(0, json['topic'],
                             json['comment'], json['username'],
                             str(datetime.now().date()),
                             False))) \
        .to_type(RequestJsonTransformer)
    container.register_value(Filter(lambda record: not record.approved)) \
        .to_type(RequestFilter)
    container.register_value(DBRequest(dbconn, engine)).to_type(DBRequest)
    container.register_type(RequestDesk, Instantiation.Singleton). \
        to_type(RequestDesk) \
        .with_params(name='requests')
    container.register_type(RequestProvider, Instantiation.Singleton). \
        to_type(RequestProvider)

    # for table request
    container.register_value(RecordTransformer(
        lambda record: TableRequest(record.id, record.number,
                                    record.date, record.username),
        lambda request: TableRequestRecord(request.id, request.number,
                                           request.date, request.username))). \
        to_type(TableRequestRecordTransformer)
    container.register_value(JsonTransformer(
        lambda json: TableRequest(0, json['number'],
                                  json['date'], json['username']))) \
        .to_type(TableRequestJsonTransformer)
    container.register_value(Filter(lambda x: True)) \
        .to_type(TableRequestFilter)
    container.register_value(DBTableRequest(dbconn, engine))\
        .to_type(DBTableRequest)
    container.register_type(TableRequestDesk, Instantiation.Singleton) \
        .to_type(TableRequestDesk).with_params(name='table_requests')
    container.register_type(TableRequestProvider, Instantiation.Singleton) \
        .to_type(TableRequestProvider)

    container.register_value(7).to_name('entry_count')

    container.register_value(DBUser(dbconn, engine)) \
        .to_type(DBUser)

    container.register_type(UserManager, Instantiation.Singleton) \
        .to_type(UserManager)

    container.register_type(UserController, Instantiation.Singleton) \
        .to_type(UserController)

    container.register_type(Authentication, Instantiation.Singleton) \
        .to_type(Authentication)

    container.register_type(RouteManager, Instantiation.Singleton) \
        .to_type(RouteManager)

    routes = container.resolve_type(RouteManager)

    app = Flask(__name__, static_folder='./static/build', static_url_path='/')
    app.config.from_object(Config)

    app.register_blueprint(routes.Routes)

    return app


app = get_app()


@app.route('/')
@app.route('/admin')
@app.route('/login')
@app.route('/request')
@app.route('/table_request')
def req():
    return app.send_static_file('index.html')

app.run(debug=True, port=8001, host='0.0.0.0')
