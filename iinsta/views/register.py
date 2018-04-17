from flask import Blueprint, render_template


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/register'
)


@bp.route('/', methods=['POST', 'GET'])
def show():
    return render_template('register.html')
