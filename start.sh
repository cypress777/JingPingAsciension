export FLASK_APP=wsgi.py
export FLASK_DEBUG=true
export APP_CONFIG_FILE=config.py
export SQLALCHEMY_TRACK_MODIFICATIONS=false
export SQLALCHEMY_DATABASE_URI='sqlite:///userinfo.db'
export SECRET_KEY='nanicypher'
flask run --port=8000