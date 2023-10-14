
import json
from flask import request

from ..config.pg_conn import pg_connection


def docs_put():

  res = { "id": None }
  
  params = request.get_json()
  
  ID = None
  try:
    if "id" in params:
      ID = int(params["id"])
  except:
    pass
  
  data = params["data"] if "data" in params else "{}"
  tag  = params["tag"]  if "tag"  in params else None

  if None != tag:

    conn, q = pg_connection()

    if None != ID:
      Q = """
        select 
          d.data 
        from 
          dev__docs d
        where
          d.id = {}
      """.format(ID)
      q.execute(Q)
      
      row = q.fetchone()
      data_curr = json.loads(row[0]) if None != row else {}
      
      data_curr.update(json.loads(data))
      data = json.dumps(data_curr)

      Q = """
        insert into 
          dev__docs (id, data)
        values 
          ({0}, '{1}') 
        on conflict (id)
        do 
          update set data = '{1}'
        returning id
      """.format(ID, data)

    else:
      
      Q = """
        insert into 
          dev__docs (data)
        values 
          ('{}') 
        returning id
      """.format(data)
    
    q.execute(Q)
    
    doc_id, = q.fetchone()
    res["id"] = doc_id

    Q = """
      insert into 
        dev__tags (tag)
      values
        ('{tag}')
      on conflict (tag)
      do 
        nothing
      ;

      insert into 
        ln_docs_tags (doc_id, tag_id)
      values
        ({doc_id}, (
          select
            id
          from 
            dev__tags
          where
            tag = '{tag}'
        ))
      on conflict (doc_id, tag_id)
      do
        nothing
    """.format(**{ "tag": tag, "doc_id": doc_id })
    q.execute(Q)
    conn.commit()
  
  return res
