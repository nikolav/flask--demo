from flask import Flask
from src.routes.index import index as route_index

app = Flask(__name__)

@app.route("/")
def home(*args):
  return route_index(*args)

if __name__ == "__main__":
  app.run(port=8001)

