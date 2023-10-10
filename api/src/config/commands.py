
from .pg_conn import pg_connection
from .sql import Q_table_main, Q_table_docs, Q_table_tags, Q_main_upsert, Q_main_upsert_admin_email, Q_table_ln_docs_tags


def cmd__db_config():
  print("running db setup...")
  conn, q = pg_connection()
  q.execute(Q_table_main)
  q.execute(Q_table_docs)
  q.execute(Q_table_tags)
  q.execute(Q_table_ln_docs_tags)
  q.execute(Q_main_upsert)
  q.execute(Q_main_upsert_admin_email)
  conn.commit()

