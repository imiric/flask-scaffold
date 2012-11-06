from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('webapp.settings.DevelopmentConfig')

import views  # don't move this, avoids circular import hell
