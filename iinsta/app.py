from flask import Flask
from iinsta.session_utils import get_current_user
from iinsta.views.api import bp as api_bp
from iinsta.views.index import bp as index_bp
from iinsta.views.register import bp as register_bp
from iinsta.views.login import bp as login_bp
from iinsta.views.feed import bp as feed_bp
from iinsta.views.account import bp as account_bp
from iinsta.views.settings import bp as settings_bp
from iinsta.views.activity import bp as activity_bp
from iinsta.views.article import bp as article_bp
from iinsta.views.search import bp as search_bp
from iinsta.views.uploads import bp as uploads_bp


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(api_bp)
app.register_blueprint(index_bp)
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(feed_bp)
app.register_blueprint(account_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(activity_bp)
app.register_blueprint(article_bp)
app.register_blueprint(search_bp)
app.register_blueprint(uploads_bp)

app.jinja_env.globals.update(get_current_user=get_current_user)
