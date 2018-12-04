
from flask import Flask
from config import config


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    init_logging(app)
    init_modules(app)

    return app

def init_modules(app):
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .item import item as item_blueprint
    app.register_blueprint(item_blueprint)

    import logging
    logging.debug("init_modules()")


def init_logging(app):
    import logging
    logging.basicConfig( filename = app.config['LOG_FILE'], level = app.config['LOG_LEVEL'] )
    logging.debug("init_logging( filename = %s, level = %i )" % (app.config['LOG_FILE'],app.config['LOG_LEVEL']))

