from flask import Flask
from src.routes.routes_init import routes_init

app = Flask(__name__)

routes_init(app)

if __name__ == "__main__":
  app.run(debug=True, port=8001)
