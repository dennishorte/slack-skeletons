import requests

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/test/', methods=['POST'])
def test_slash_command():
    """
    Data is received in the form of a dictionary in the request.form variable.
    Must return success. Can optionally include an immediate response.
    """
    data = request.form
    print('----------------------------------------------')
    print(data)

    return jsonify(
        success=True,
        response_type="in_channel",
        text="received test slash command",
    )
