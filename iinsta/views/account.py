from flask import Blueprint, render_template


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/<account_name>')
def show(account_name):
    return render_template('account.html')
