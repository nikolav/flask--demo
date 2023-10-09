
from random import randint
from ..config.pg_conn import pg_connection
from ..config.sql import Q__admin_email


def index():

  conn, q = pg_connection()

  q.execute(Q__admin_email)
  value, = q.fetchone()

  res = { 
    "status": "ok",
    "admin:email": value,
    "data": randint(1, 9999)
  }

  return res
