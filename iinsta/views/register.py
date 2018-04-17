from flask import Blueprint, render_template, request
from iinsta.forms.RegisterForm import RegisterForm


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/register'
)


@bp.route('/', methods=['POST', 'GET'])
def show():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        print('form')

    return render_template('register.html', form=form)
