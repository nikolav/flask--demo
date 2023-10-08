import psycopg2 as pg
from .vars import DB_URI

_conn = None
_q = None

def pg_connection():

  global _conn
  global _q

  if None == _conn:
    _conn = pg.connect(DB_URI)
    _q = _conn.cursor()
  
  return _conn, _q
