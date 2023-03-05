from starlette.routing import Route
from . import views

patterns = [
    Route("/", views.index),
]