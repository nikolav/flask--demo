
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
  tag_id  bigint     not null, 

  unique (doc_id, tag_id)
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
  dev__docs d
    join
      ln_docs_tags l
        on
          l.doc_id = d.id
    join
      dev__tags t
        on
          l.tag_id = t.id
where
  t.tag = '{}'
"""

Q__drop_doc_by_id = """
delete from dev__docs
where
  id = {}
"""

Q__drop_docs_tags_by_docid = """
delete from ln_docs_tags
where
  doc_id = {}
"""

Q__find_doc_by_id = """
  select 
    *
  from
    dev__docs
  where
    id = '{}'
"""

Q__tags_by_doc_id = """
  select 
    t.tag tag
  from
    dev__tags t
      join
        ln_docs_tags l
          on
            l.tag_id = t.id
      join
        dev__docs d
          on
            l.doc_id =d.id
  where
    d.id = '{}'
"""

