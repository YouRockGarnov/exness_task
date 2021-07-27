from flask import (
    Flask,
    jsonify,
    json,
    make_response,
    request
)
from flask_smorest import Api
from app.resources import blueprint as calculate_blueprint


app = Flask(__name__)
app.config.from_object("config.Config")

# if you just import app then it will be fixed. Use get_app to get the updated app.
def get_app():
    return app


api = Api(app)
api_prefix = '/api'
api.register_blueprint(calculate_blueprint, url_prefix=api_prefix)


@app.errorhandler(Exception)
def handle_exception(error):
    return make_response(jsonify({'message': str(error)}), 500)

