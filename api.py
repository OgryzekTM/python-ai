import json

from flask import Flask
from flask import request
from werkzeug.utils import secure_filename
from detect import detect
import os

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    f.save('/uploads/' + secure_filename(f.filename) + ".png")
    result = detect('/uploads/' + secure_filename(f.filename) + ".png")
    os.remove('/uploads/' + secure_filename(f.filename) + ".png")
    return json.dumps({"result": result})
