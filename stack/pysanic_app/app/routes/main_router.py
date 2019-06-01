from sanic.response import json
from sanic import Blueprint
from sanic_openapi import doc

from app.config.logger.app_logger import logger

from functools import wraps
import multiprocessing

bp = Blueprint(name='main_router')


class Car:
    details = str
    name = str
    speed = int

    def __init__(self, details: str, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.details = details


def logged_request():
    def decorator(f):
        @wraps(f)
        async def handler(request, *args, **kwargs):
            return await f(request, *args, **kwargs)

        return handler

    return decorator


@doc.produces(Car)
@bp.route("/")
@logged_request()
async def test(request):
    logger.info("Available CPU's = %s", multiprocessing.cpu_count())
    return json(Car(details='This is a car', name='Opel', speed=120))
