from litestar import Litestar, Request
from litestar.config.cors import CORSConfig
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_401_UNAUTHORIZED
from litestar_piccolo import PiccoloPlugin

from app.controllers.product import ProductController
from piccolo_conf import open_database_connection_pool, close_database_connection_pool


def internal_server_error_handler(request: Request, exc: Exception):
    raise exc


cors_config = CORSConfig(allow_origins=["*"])

piccolo = PiccoloPlugin()
app = Litestar(
    plugins=[piccolo],
    route_handlers=[ProductController],
    cors_config=cors_config,
    exception_handlers={
        HTTP_500_INTERNAL_SERVER_ERROR: internal_server_error_handler,
        HTTP_401_UNAUTHORIZED: internal_server_error_handler,
    },
    on_startup=[open_database_connection_pool],
    on_shutdown=[close_database_connection_pool],
)
