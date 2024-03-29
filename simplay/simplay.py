import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

_DIR_NAME = "data"
_DATA_ROOT_DIR = os.path.abspath(os.path.normpath(os.path.join(os.path.dirname(__file__), _DIR_NAME)))

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config.from_object("simplay.settings")

csrf = CSRFProtect(app)

def get_data_file(filename):
    return os.path.join(_DATA_ROOT_DIR, filename)