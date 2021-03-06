from flask import Blueprint, jsonify, request
from bson.objectid import ObjectId
import json
from iinsta.facades.ArticleFacade import ArticleFacade
from iinsta.facades.UserFacade import UserFacade
from iinsta.session_utils import get_current_user, login_required


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/api'
)


@bp.route('/article/<article_id>', methods=['GET'])
@login_required
def show_article(article_id):
    _article = ArticleFacade.get(id=ObjectId(article_id))

    if not _article:
        return jsonify(None)

    article = json.loads(_article.to_json())
    article['comments'] = []

    for _comment in _article.comments:
        comment = json.loads(_comment.to_json())
        comment['user'] = json.loads(_comment.user.to_json())
        article['comments'].append(comment)

    return jsonify(article)


@bp.route('/article/comment/<article_id>', methods=['POST', 'GET'])
@login_required
def show_article_comment(article_id):
    user = get_current_user()
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data received'}), 400

    if 'content' not in data:
        return jsonify({'error': 'Missing field `content`'}), 400

    article = ArticleFacade.get(id=ObjectId(article_id))

    article.comment(user=user, content=data['content'])

    article = ArticleFacade.get(id=ObjectId(article_id))

    return jsonify(json.loads(article.to_json()))


@bp.route('/article/like/<article_id>', methods=['POST', 'GET'])
@login_required
def show_article_like(article_id):
    user = get_current_user()

    article = ArticleFacade.get(id=ObjectId(article_id))

    if user not in article.likers:
        article.like(user=user)
    else:
        article.unlike(user=user)

    article = ArticleFacade.get(id=ObjectId(article_id))

    return jsonify(json.loads(article.to_json()))


@bp.route('/article/delete/<article_id>', methods=['POST', 'GET'])
@login_required
def show_article_delete(article_id):
    user = get_current_user()

    article = ArticleFacade.get(id=ObjectId(article_id))

    if user != article.user:
        return jsonify({'error': 'Not authorized'}), 401

    article.delete()

    return jsonify({'success': True})


@bp.route('/search/<query>', methods=['GET', 'POST'])
@login_required
def show_search(query):
    results = []
    users = list(UserFacade.search(query))
    articles = ArticleFacade.search(query)

    for article in articles:
        for tag in article.tags:
            if tag not in results and query.lower() in tag.lower():
                results.append(tag)

    for i, user in enumerate(users):
        _user = json.loads(user.to_json())
        _user['avatar'] = json.loads(user.avatar.to_json()) if user.avatar\
            else None
        del _user['password']

        results.append(_user)

    return jsonify(results)
