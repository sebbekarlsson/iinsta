from flask import Blueprint, render_template
from iinsta.session_utils import login_required, get_current_user
from iinsta.facades.ArticleFacade import ArticleFacade
from iinsta.facades.UserFacade import UserFacade


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/feed/<tag>')
@bp.route('/feed', defaults={'tag': None})
@login_required
def show(tag):
    current_user = get_current_user()
    following = list(UserFacade.get_all(query={'followers': current_user}))
    following.append(current_user)

    article_query = {}

    if tag:
        article_query['tags'] = tag
    else:
        article_query['user__in'] = following

    articles = ArticleFacade.get_all(query=article_query)

    return render_template('feed.html', articles=articles)
