from flask import Blueprint, render_template
from iinsta.session_utils import login_required, get_current_user
from iinsta.facades.ArticleFacade import ArticleFacade
from iinsta.facades.UserFacade import UserFacade


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/feed')
@login_required
def show():
    current_user = get_current_user()
    following = UserFacade.get_all(query={'followers': current_user})

    articles = ArticleFacade.get_all(query={'user__in': following})

    return render_template('feed.html', articles=articles)
