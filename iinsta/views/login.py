from flask import Blueprint, render_template, request, session, redirect
from iinsta.forms.LoginForm import LoginForm
from iinsta.password import check_password
from iinsta.facades.UserFacade import UserFacade


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
        user = UserFacade.get(name=form.name.data)

        if not user:
            errors.append('Wrong credentials')
        else:
            if not check_password(user['password'], form.password.data):
                errors.append('Wrong credentials')
            else:
                session['user_id'] = str(user.id)

                return redirect('/')

    return render_template('login.html', form=form, errors=errors)


@bp.route('/logout')
def show_logout():
    session['user_id'] = None
    del session['user_id']

    return redirect('/')
