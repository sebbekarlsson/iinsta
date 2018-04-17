from flask import Blueprint, render_template, request


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/<account_name>', methods=['POST', 'GET'])
def show(account_name):
    if request.method == 'POST':
        if request.form.get('follow'):
            print('follow')

    return render_template('account.html')
