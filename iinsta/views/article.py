from flask import Blueprint, render_template, request
from iinsta.session_utils import login_required, get_current_user
from iinsta.forms.ArticleEditForm import ArticleEditForm


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/article'
)


@bp.route('/', methods=['POST', 'GET'])
@login_required
def show_edit():
    user = get_current_user()
    errors = []
    form = ArticleEditForm(request.form)

    if request.method == 'POST' and form.validate():
        pass

    return render_template(
        'article_edit.html',
        form=form,
        user=user,
        errors=errors
    )
