import os

from flask import Flask
from flask_restful import Api


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "tagrest.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    # register the database commands
    from tagrest import db

    db.init_app(app)

    api = Api(app)

    from tagrest import resources
    api.add_resource(resources.Hash, "/hash/<string:kind>/<string:tag>/<int:runnumber>", methods=("GET", "POST"))
    api.add_resource(resources.Payload, "/payload/<string:hash>", methods=("GET", "POST"))
    api.add_resource(resources.TagMap, "/tagmap/<string:globaltag>")
    api.add_resource(resources.GlobalTag, "/globaltag/<string:globaltag>", methods=("GET", "POST"))

    ################## EXPERIMENTAL ##################
    api.add_resource(resources.FastTagMap, "/fasttagmap/<string:globaltag>")
    api.add_resource(resources.Test, "/test")


    return app


