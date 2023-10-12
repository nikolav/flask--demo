

from flask import request

from ..config.pg_conn  import pg_connection
from ..config.sql      import Q__list_docs_by_tag


def docs_ls():

  res = []

  try:

    tag = request.args.get("tag")

    if None == tag:
      raise Exception
      
    conn, q = pg_connection()
    
    q.execute(Q__list_docs_by_tag.format(tag))
    res = q.fetchall()

  except:
    pass
  else:
    conn.commit()

  return res
