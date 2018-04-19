from flask import Blueprint, render_template, request, redirect
from iinsta.session_utils import login_required, get_current_user
from iinsta.asset_utils import upload_file
from iinsta.forms.ArticleEditForm import ArticleEditForm
from iinsta.facades.ArticleFacade import ArticleFacade
from iinsta.facades.AssetFacade import AssetFacade


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
        if 'media' not in request.files:
            errors.append('An image is required')
        else:
            new_name = upload_file(request.files['media'])
            asset = AssetFacade.create(name=new_name, filename=new_name)

            kwargs = {
                'media': asset,
                'content': form.content.data,
                'user': user
            }

            article = ArticleFacade.create(**kwargs)
            return redirect('/article/' + str(article.id))

    return render_template(
        'article_edit.html',
        form=form,
        user=user,
        errors=errors
    )
