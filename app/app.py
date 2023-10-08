
from flask import Flask, send_from_directory, send_file

app = Flask(__name__)

@app.route("/")
def home():
  return send_file("static/index.html")

@app.route("/<path:path>")
def static_resource(path):
  return send_from_directory("static", path)

if __name__ == "__main__":
  app.run(port=8000)
