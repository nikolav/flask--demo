
from flask import request

from ..config.pg_conn import pg_connection
from ..config.sql     import Q__drop_doc_by_id, Q__drop_docs_tags_by_docid


def docs_rm():

  res = { "id": None, "rows_deleted": 0 }
  
  try:

    params = request.get_json()
    doc_id = int(params["id"])
    
    if None != doc_id:

      res["id"] = doc_id

      conn, q = pg_connection()

      q.execute(Q__drop_doc_by_id.format(doc_id))
      res["rows_deleted"] = q.rowcount
      
      if 0 < q.rowcount:
        q.execute(Q__drop_docs_tags_by_docid.format(doc_id))

  except:
    pass

  finally:
    conn.commit()
  
  return res

