# APP_REGISTRY = AppRegistry(apps=["piccolo.apps.user.piccolo_app"])
from piccolo.conf.apps import AppRegistry
from piccolo.engine import PostgresEngine

from settings import settings

DB = PostgresEngine(
    config={
        "database": settings.db_name,
        "user": settings.db_user,
        "password": settings.db_password,
        "host": settings.db_host,
        "port": settings.db_port,
    }
)


async def open_database_connection_pool():
    await DB.start_connection_pool()


async def close_database_connection_pool():
    await DB.close_connection_pool()


APP_REGISTRY = AppRegistry(apps=["app.piccolo_app"])
