from flask import Flask
from flask_restful import Api
from slowrest.cache import cache
from slowrest.resources import add_dynamic_resource
from slowrest.utils import get_page_sensor_dict


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)
    app.config.from_prefixed_env()

    # register the database commands
    from slowrest import db

    db.init_app(app)
    # configure the DB queries
    from slowrest import queries

    for name in [x for x in dir(queries) if not x.startswith("__")]:
        q = getattr(queries, name).replace("__PREFIX__", app.config["prefix"])
        setattr(queries, name, q)

    # configure cache
    cache_config = {"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 15}
    cache.init_app(app, config=cache_config)

    api = Api(app)

    from slowrest import resources

    api.add_resource(resources.Index, "/")
    api.add_resource(resources.SensorDict, "/sensor-dict")
    api.add_resource(resources.SensorName, "/sensor-name/<int:sensor_id>")
    api.add_resource(resources.Day, "/day/<string:day>/<int:sensor_id>")
    api.add_resource(
        resources.Range, "/range/<string:begin>/<string:end>/<int:sensor_id>"
    )

    # Dynamically create new pages based on sensor list files
    for sensor_list_name, sensor_id_list in get_page_sensor_dict().items():
        add_dynamic_resource(
            api, sensor_list_name, sensor_id_list, f"/latest/{sensor_list_name}"
        )

    return app
