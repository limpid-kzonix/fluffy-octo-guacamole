from sanic import Sanic

from app.config.logger.app_logger import LOGGING_CONFIG_SERVER
from sanic_openapi import swagger_blueprint

from app.routes.main_router import bp

app = Sanic(
    name=__name__,
    log_config=LOGGING_CONFIG_SERVER
)

app.blueprint(swagger_blueprint)
app.blueprint(blueprint=bp)