from flask import Flask
from flask_cors import CORS
import psycopg2 as pg
from src.config.vars import DB_URI


app = Flask(__name__)
CORS(app)

SQL = """
  select 1+2 as sum
"""

@app.route("/")
def home():
  conn = pg.connect(DB_URI)
  q = conn.cursor()
  q.execute(SQL)
  sum, = q.fetchone()
  res = { "status": "ok", "data": sum }
  return res


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)
