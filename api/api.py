from flask import Flask
from flask_cors import CORS
from src.config.pg_conn import conn, q


app = Flask(__name__)
CORS(app)

SQL = """
  select 1+2 as sum
"""

@app.route("/")
def home():
  q.execute(SQL)
  sum, = q.fetchone()
  res = { "status": "ok", "data": sum }
  return res


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
