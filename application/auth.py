from flask import redirect, render_template, flash, Blueprint, request, url_for
from flask_login import login_required, logout_user, current_user, login_user
from flask import current_app as app
from werkzeug.security import generate_password_hash
from .models import db, User
from . import login_manager

auth_bp = Blueprint('auth_bp', __name__,
                    template_folder='templates',
                    static_folder='static')

@auth_bp.route('/login', methods=['GET', 'POST'])
def Login():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.Game', username=current_user.name))

    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(name=username).first()
        if user:
            if user.check_password(password=password):
                login_user(user)
                return redirect(url_for('main_bp.Game', username=current_user.name))
        error = 'Invalid log in: Wrong username/password'
        flash(error)
        return redirect(url_for('auth_bp.Login'))
    else:
        return render_template('user_access.html', title='Login', ngApp='userAccessApp', ngCtrl='userAccessController')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def Signup():
    if current_user.is_authenticated:
        return redirect(url_for('main_bp.Game', username=current_user.name))
    error = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        existing_user = User.query.filter_by(name=username).first()
        if existing_user is None:
            user = User(name=username,
                        password=generate_password_hash(password,  method='sha256'))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth_bp.Login'))
        else:
            error = 'Invalid sign up: Username has been taken'
            flash(error)
            return redirect(url_for('auth_bp.Signup'))
    else:
        return render_template('user_access.html', title='Signup', ngApp='userAccessApp', ngCtrl='userAccessController')

@auth_bp.route("/logout")
@login_required
def logout_page():
    logout_user()
    return redirect(url_for('auth_bp.Login'))


@login_manager.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.Login'))