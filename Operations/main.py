import logging
from flask import Flask, render_template, request, redirect, flash
from flask_wtf.csrf import CSRFProtect
from flask_csp.csp import csp_header
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_cors import CORS
from forms import MovieForm
import requests

app = Flask(__name__)
app.secret_key = b"hSWrqNxeExuR03aq;apl"
csrf = CSRFProtect(app)
limiter = Limiter(get_remote_address, app=app)
cors = CORS(app) 
app.config["CORS_HEADERS"] = "Content-Type"
headers = {"Authorisation": "uPTPeF9BDNiqAkNj"}  # Add your API key


# Initialize logging
app_log = logging.getLogger(__name__)
logging.basicConfig(
    filename="security_log.log",
    encoding="utf-8",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)

# Secure cookie settings
app.config.update(
    SESSION_COOKIE_SECURE=True,  # Ensure cookies are only sent over HTTPS
    SESSION_COOKIE_HTTPONLY=True,  # Prevent JavaScript access to cookies
    SESSION_COOKIE_SAMESITE='Lax',  # Control how cookies are sent with cross-site requests
)

# Redirect index.html to domain root for consistent UX
@app.route("/index", methods=["GET"])
@app.route("/index.htm", methods=["GET"])
@app.route("/index.asp", methods=["GET"])
@app.route("/index.php", methods=["GET"])
@app.route("/index.html", methods=["GET"])
def root():
    return redirect("/", 302)  # Redirect to the root URL

@app.route("/", methods=["GET", "POST"])
@csp_header(
    {
        "base-uri": "'self'",
        "default-src": "'self'",
        "style-src": "'self'",
        "script-src": "'self'",
        "img-src": "'self' data:",
        "media-src": "'self'",
        "font-src": "'self'",
        "object-src": "'self'",
        "child-src": "'self'",
        "connect-src": "'self'",
        "worker-src": "'self'",
        "report-uri": "/csp_report",
        "frame-ancestors": "'none'",
        "form-action": "'self'",
        "frame-src": "'none'",
        "manifest-src": "'self'",
    }
)
def predict():
    form = MovieForm()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                # Extract form data
                data = {
                    "budget": form.budget.data,
                    "release_date": form.release_date.data,
                    "rating": form.rating.data,
                    "is_sequel": form.is_sequel_data,
                    "runtime": form.runtime.data,
                    "genre": form.genre.data,
                }
                # Send data to the API
                response = requests.post("http://127.0.0.1:3000/api/prediction", json=data, headers=headers)
                if response.status_code == 200:
                    flash(f"Prediction: {response.json()['prediction']}", "success")
                else:
                    app_log.error(f"API Error: {response.json().get('message', 'Unknown error')}")
                    flash(f"API Error: {response.json().get('message', 'Unknown error')}","danger",)
            else:
                # Log form validation errors
                app_log.error(f"Form validation errors: {form.errors}")
                flash("Please correct the errors in the form and try again.", "danger")
        except requests.exceptions.RequestException as e:
            app_log.error(f"Error connecting to API: {str(e)}")
            flash("An error occurred while connecting to the API. Please try again later.","danger",)
        except Exception as e:
            app_log.error(f"Unexpected error: {str(e)}")
            flash("An unexpected error occurred. Please try again later.", "danger")
        return redirect("/")
    elif request.method == "GET":
        return render_template("index.html", form=form)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)