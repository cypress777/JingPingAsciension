export FLASK_APP=wsgi.py
export FLASK_DEBUG=false
export APP_CONFIG_FILE=config.py
export SQLALCHEMY_TRACK_MODIFICATIONS=false
export LC_ALL='en_US.utf-8'
python3 -m flask run --port=8000 --host=0.0.0.0
