from flask import Flask, jsonify

from flaskr.rest import rest

app = Flask(__name__)

app.register_blueprint(rest)


if __name__ == '__main__':
    app.run(debug=True)