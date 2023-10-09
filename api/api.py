from flask import Flask
from flask_cors import CORS
from src.routes.routes_init import routes_init


app = Flask(__name__)
CORS(app)

routes_init(app)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
