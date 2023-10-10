
from random import randint


Q_table_main = """
  create table if not exists dev__main (
    id     bigserial  primary key,
    name   text       unique,
    value  text
  )
"""

Q_table_docs = """
  create table if not exists dev__docs (
    id     bigserial  primary key,
    docid  text       unique null,
    data   text
  )
"""

Q_table_tags = """
  create table if not exists dev__tags (
    id   bigserial  primary key,
    tag  text       unique not null
  )
"""

Q_table_ln_docs_tags = """
create table if not exists ln_docs_tags (
  id      bigserial  primary key,
  doc_id  bigint     not null,
  tag_id  bigint     not null
)
"""

Q_main_upsert = """
  insert into dev__main
    (name, value)
  values 
    ('test', 'test')
  on conflict (name)
  do
    update set value = 'test.{}'
""".format(randint(1, 99))

Q_main_upsert_admin_email = """
  insert into dev__main
    (name, value)
  values 
    ('admin:email', 'admin@nikolav.rs')
  on conflict (name)
  do
    update set value = 'admin@nikolav.rs'
"""

Q__admin_email = """
  select 
    value 
  from
    dev__main
  where
    name = 'admin:email'
  limit 1
"""

Q__list_docs_by_tag = """
  select 
  d.*
from 
  dev__docs as d
JOIN
  ln_docs_tags as l
on
  l.doc_id = d.id
JOIN
  dev__tags as t
on
  l.tag_id = t.id
where
  t.tag = '{}'
"""
