from flask import Flask
from views import views
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generates a random key
app.register_blueprint(views, url_prefix = "/")

if __name__ == '__main__':
    app.run(debug=True)

