import os
from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import app_config

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
ma = Marshmallow()
migrate = Migrate()
login_manager = LoginManager()

TEMPLATES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
STATIC_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')


def create_app(config_name=os.environ['APP_ENV']):
    app = Flask(__name__, instance_relative_config=True, static_folder=STATIC_FOLDER, template_folder=TEMPLATES_FOLDER)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)


    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    from .auth.resource import auth as auth_blueprint

    app.register_blueprint(auth_blueprint)

    return app