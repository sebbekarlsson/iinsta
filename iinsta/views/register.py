from flask import Blueprint, render_template, request, session, redirect
from iinsta.password import get_hashed_password
from iinsta.forms.RegisterForm import RegisterForm
from iinsta.facades.UserFacade import UserFacade


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/register'
)


@bp.route('/', methods=['POST', 'GET'])
def show():
    errors = []
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        if UserFacade.exists(name=form.name.data):
            errors.append('User already exists')
        else:
            user = UserFacade.create(
                name=form.name.data,
                firstname=form.firstname.data,
                lastname=form.lastname.data,
                password=get_hashed_password(form.password.data)
            )

            session['user_id'] = str(user.id)

            return redirect('/')

    return render_template('register.html', form=form, errors=errors)
