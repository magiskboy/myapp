from starlette.requests import Request
from starlette.responses import PlainTextResponse

def index(request: Request):
    return PlainTextResponse("Hello world")