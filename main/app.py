from starlette.applications import Starlette
from starlette.schemas import SchemaGenerator

from common import import_string

from .setting import get_setting
from . import db
from .register import registers


def create_app(name_setting = "production") -> Starlette:
    setting = get_setting(name_setting)

    def on_startup():
        db.connect(setting.DATABASE_URI)

    def on_shutdown():
        db.disconnect()

    app = Starlette(
        debug=setting.DEBUG,
        on_startup=[on_startup],
        on_shutdown=[on_shutdown],
    )

    # OpenAPI doc view
    schema_generator = SchemaGenerator({"openapi": "3.0.0", "info": {"title": "MyApp", "version": "1.0"}})
    def openapi_handler(request):
        return schema_generator.OpenAPIResponse(request)
    app.add_route("/schema.yaml", openapi_handler, methods=["GET"])

    # register sub-app
    for path, mod_path in registers:
        mod = import_string(mod_path)
        subapp = Starlette(
            debug=setting.DEBUG,
            routes=mod.patterns,
        )
        app.mount(path, subapp, mod.name)

    return app
