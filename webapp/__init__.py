from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from helpers import LazyView

app = Flask(__name__)
app.config.from_object('settings.DevelopmentConfig')
db = SQLAlchemy(app)

def url(url_rule, import_name, **options):
    view = LazyView(import_name)
    app.add_url_rule(url_rule, view_func=view, **options)

import routes # don't move this, avoids circular import hell
