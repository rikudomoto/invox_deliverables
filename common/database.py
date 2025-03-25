from typing import Any

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from common.models import load_models
db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app, db)

    load_models()

BaseModel = db.Model

class HasStandardSetting:
    def __init__(self, *args, **kwargs: Any):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<{self.__class__} ()>"