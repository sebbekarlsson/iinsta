from flask import Blueprint, render_template
from iinsta.session_utils import login_required


bp = Blueprint(
    __name__,
    __name__,
    template_folder='templates',
    url_prefix='/search'
)


@bp.route('/', methods=['POST', 'GET'])
@login_required
def show_search():
    return render_template('search.html')
