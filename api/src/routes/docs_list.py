

from flask import request

from ..config.pg_conn  import pg_connection
from ..config.sql      import Q__list_docs_by_tag


def docs_list():

  res = None

  params = request.get_json()
  conn, q = pg_connection()

  try:
    q.execute(Q__list_docs_by_tag.format(params['tag']))
    res = q.fetchall()
  except:
    pass
  else:
    conn.commit()

  return res
