# -*- coding: utf-8 -*-
from fabric.api import local
from fabric.state import output

output['status'] = False

def run():
    """Starts local development server"""
    from webapp import app
    from werkzeug.serving import run_simple

    if app.debug:
        run_simple('0.0.0.0', 5000, app,
            use_reloader=True, use_debugger=True, use_evalex=True)
    else:
        app.run(host='0.0.0.0')

def clean():
    """Removes all unnecessary files"""
    local('find . -name "*.pyc" -type f -exec rm {} \;')
