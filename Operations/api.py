import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from model import MLModel

api = Flask(__name__)
cors = CORS(api)
api.config["CORS_HEADERS"] = "Content-Type"
auth_key = "uPTPeF9BDNiqAkNj"
limiter = Limiter(
    get_remote_address,
    app=api,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://",
)

MLmodel = MLModel()
MLmodel.load_model("path/to/your/model.pkl")

# Initialize logging
app_log = logging.getLogger(__name__)
logging.basicConfig(
    filename="api_security_log.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)

def check_api_key():
    if request.headers.get("Authorisation") != auth_key:
        return jsonify({"message": "Invalid or missing API key"}), 401
    

@api.route("/api/prediction", methods=["POST"])
@limiter.limit("1/second", override_defaults=False)
def prediction():
    auth_response = check_api_key()
    if auth_response:
        return auth_response
    try:
        data = request.get_json()
        if not data:
            return jsonify({"message": "No input data provided"}), 400
        prediction = MLmodel.predict(data)
        return jsonify({"prediction": prediction})
    except Exception as e:
        app_log.error(f"Error in prediction: {e}")
        return jsonify({"message": "Error processing the request"}), 500

@api.route("/api/setData", methods=["POST"])
@limiter.limit("1/second", override_defaults=False)
def setData():
    auth_response = check_api_key()
    if auth_response:
        return auth_response