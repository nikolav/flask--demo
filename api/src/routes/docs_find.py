
import json

from ..config.pg_conn import pg_connection
from ..config.sql     import Q__find_doc_by_id, Q__tags_by_doc_id


def docs_find(ID):

  res = { "exists": False }

  try:

    conn, q = pg_connection()
    
    q.execute(Q__find_doc_by_id.format(ID))
    
    record = q.fetchone()
    if None != record:
      
      q.execute(Q__tags_by_doc_id.format(ID))
      tags = q.fetchall()
      
      ID, data = record

      res["exists"] = True
      res["id"] = ID
      res["data"] = json.loads(data)
      res["tags"] = [t for t, in tags]

  except:
    pass
  
  finally:
    if None != conn:
      conn.commit()

  return res
