from flask import Blueprint, render_template, request
import os
from iinsta.config import config
from iinsta.session_utils import login_required, get_current_user
from iinsta.asset_utils import upload_file
from iinsta.forms.ProfileEditForm import ProfileEditForm
from iinsta.facades.UserFacade import UserFacade
from iinsta.facades.AssetFacade import AssetFacade
from iinsta.facades.ArticleFacade import ArticleFacade


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/<account_name>', methods=['POST', 'GET'])
@login_required
def show(account_name):
    current_user = get_current_user()
    user = UserFacade.get(name=account_name)

    if not user:
        return 'No such user', 404

    articles = ArticleFacade.get_all(query={'user': user})

    if request.method == 'POST':
        if request.form.get('follow'):
            if current_user in user.followers:
                user.unfollow(user=current_user)
            else:
                user.follow(user=current_user)

    return render_template('account.html', user=user, articles=articles)


@bp.route('/<account_name>/edit', methods=['POST', 'GET'])
@login_required
def show_edit(account_name):
    user = get_current_user()

    if account_name != user.name:
        return 'Not Authorized', 401

    errors = []
    form = ProfileEditForm(request.form)

    if request.method == 'POST' and form.validate():
        kwargs = {
            'firstname': form.firstname.data,
            'lastname': form.lastname.data,
            'bio': form.bio.data,
            'website': form.website.data
        }

        if 'avatar' in request.files:
            if user.avatar:
                avatar_path = os.path.join(
                    config['uploads_dir'],
                    user.avatar.filename
                )

                if os.path.isfile(avatar_path):
                    os.remove(avatar_path)

                user.avatar.delete()

            new_name = upload_file(request.files['avatar'])
            asset = AssetFacade.create(
                name=new_name,
                filename=new_name
            )

            kwargs['avatar'] = asset

        user.update(**kwargs)
        user.save()

        user = get_current_user()

    form.firstname.data = user.firstname
    form.lastname.data = user.lastname
    form.bio.data = user.bio
    form.website.data = user.website

    return render_template(
        'account_edit.html',
        form=form,
        errors=errors,
        user=user
    )
