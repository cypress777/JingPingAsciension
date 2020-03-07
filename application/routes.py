from flask import Blueprint, render_template
from flask_login import current_user
from flask import current_app as app
from flask_login import login_required

main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@main_bp.route('/', methods=['GET', 'POST'])
@main_bp.route('/en', methods=['GET', 'POST'])
def Welcome():
  return render_template('hello.html', title='Welcome to Ascension', ngApp='helloApp', ngCtrl='helloController')

@main_bp.route('/game', methods=['GET', 'POST'])
@login_required
def Game():
  return render_template('game.html', welcome_info='Welcome Back', username=current_user.name, title='Game',
                        ngApp='gameApp', ngCtrl='gameCtrl')
