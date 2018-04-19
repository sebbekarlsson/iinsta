from flask import Blueprint, render_template, request
from iinsta.session_utils import login_required
from iinsta.forms.ProfileEditForm import ProfileEditForm


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/<account_name>', methods=['POST', 'GET'])
@login_required
def show(account_name):
    if request.method == 'POST':
        if request.form.get('follow'):
            print('follow')

    return render_template('account.html')


@bp.route('/<account_name>/edit', methods=['POST', 'GET'])
@login_required
def show_edit(account_name):
    errors = []
    form = ProfileEditForm(request.form)

    if request.method == 'POST' and form.validate():
        pass

    return render_template('account_edit.html', form=form, errors=errors)
