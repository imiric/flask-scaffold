from webapp import app
from werkzeug.serving import run_simple

if app.debug:
    run_simple('0.0.0.0', 5000, app,
        use_reloader=True, use_debugger=True, use_evalex=True)
else:
    app.run(host='0.0.0.0')
