from ..config.pg_conn import conn, q

SQL = """
  select 
    value 
  from
    main
  where
    name = 'admin.email'
  limit 1
"""


def admin_email():
  res = None
  try:
    q.execute(SQL)
  except Exception as err:
    raise err
  else:
    value, = q.fetchone()
    res = { "admin.email": value }
  
  return res
