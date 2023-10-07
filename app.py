from flask import Flask
from src.routes.setup import setup as setup_routes

app = Flask(__name__)

setup_routes(app)

if __name__ == "__main__":
  app.run(debug=True, port=8001)
