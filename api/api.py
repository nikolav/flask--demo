from flask import Flask
from src.routes.routes_init import routes_init
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

routes_init(app)

if __name__ == "__main__":
  app.run(port=5000)
