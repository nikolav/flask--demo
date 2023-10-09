
from random import randint


Q__admin_email = """
  select 
    value 
  from
    main
  where
    name = 'admin.email'
  limit 1
"""

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

Q_main_upsert = """
  insert into dev__main
    (name, value)
  values 
    ('test', 'test')
  on conflict (name)
  do
    update set value = 'test.{}'
""".format(randint(1, 99))
