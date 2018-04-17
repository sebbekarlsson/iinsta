from flask import Flask
from iinsta.views.index import bp as index_bp
from iinsta.views.feed import bp as feed_bp
from iinsta.views.account import bp as account_bp


app = Flask(__name__)

app.config.update(
    SECRET_KEY='abc123',
    TEMPLATES_AUTO_RELOAD=True
)

app.register_blueprint(index_bp)
app.register_blueprint(feed_bp)
app.register_blueprint(account_bp)
