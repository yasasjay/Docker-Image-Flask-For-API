from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from api import application
import os
app = Flask(__name__)

CORS(app)

app.register_blueprint(application)

@app.route('/')
def default_route():
    return "Welcome to the default route!"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)