from flask import Blueprint, render_template

comment_bp = Blueprint('comment', __name__, template_folder='templates')

@comment_bp.route('/')
def index():
    return render_template('comment/index.html')
