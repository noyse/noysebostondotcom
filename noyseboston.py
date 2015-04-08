from flask import (
    Flask,
    render_template,
)
from flask.ext.assets import Environment, Bundle
from werkzeug.contrib.fixers import ProxyFix
import settings

app = Flask(__name__)

assets = Environment(app)
app.debug = settings.DEBUG
assets.url = app.static_url_path
app.wsgi_app = ProxyFix(app.wsgi_app)
scss = Bundle('scss/concise-noyse.scss', filters='pyscss', output='css/main.css')
assets.register('scss_all', scss)


def get_base_context():
    return {
        'title': "NOYSE BOSTON",
    }

@app.route('/')
def index():
    context = get_base_context()
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run()
