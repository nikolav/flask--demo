from flask import Flask, send_from_directory, send_file
from config.vars import DIR_STATIC


app = Flask(__name__)

@app.route("/")
def home():
  return send_file("{}/index.html".format(DIR_STATIC))

@app.route("/<path:path>")
def static_resource(path):
  return send_from_directory(DIR_STATIC, path)

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
