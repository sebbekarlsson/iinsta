from flask import Blueprint, render_template, request, session, redirect
from iinsta.forms.LoginForm import LoginForm


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates'
)


@bp.route('/login', methods=['POST', 'GET'])
def show():
    errors = []
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        pass

    return render_template('login.html', form=form, errors=errors)


@bp.route('/logout')
def show_logout():
    session['user_id'] = None
    del session['user_id']

    return redirect('/')
