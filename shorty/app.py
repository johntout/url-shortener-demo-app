from flask import Flask
from shorty.api import api
from dotenv import load_dotenv

def create_app(settings_overrides=None):
    app = Flask(__name__)
    configure_settings(app, settings_overrides)
    configure_blueprints(app)
    load_dotenv()
   
    return app


def configure_settings(app, settings_override):
    app.config.update({
        'DEBUG': True,
        'TESTING': False,
    })
    if settings_override:
        app.config.update(settings_override)


def configure_blueprints(app):
    app.register_blueprint(api)
