from flask import Flask

from app.users.urls import mod_user


__all__ = [
    'AppFactory',
    'app_factory',
]


class AppFactory(object):

    def __init__(self):
        self.app = Flask(
            __name__,
        )
        # Load config
        self.app.config.from_object('config')
        self.configure_views()

    def configure_views(self):
        self.app.register_blueprint(mod_user)


app_factory = AppFactory()
