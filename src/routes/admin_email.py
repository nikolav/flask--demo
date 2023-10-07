from ..config.pg_conn import conn, q
from ..config.sql     import Q__admin_email


def admin_email():
  res = None
  try:
    q.execute(Q__admin_email)
  except Exception as err:
    raise err
  else:
    value, = q.fetchone()
    res = { "admin.email": value }
  
  return res
