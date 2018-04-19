from flask import Blueprint, render_template
from iinsta.session_utils import login_required
from iinsta.facades.ArticleFacade import ArticleFacade


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/feed')
@login_required
def show():
    articles = ArticleFacade.get_all()

    return render_template('feed.html', articles=articles)
