import psycopg2 as pg
from .vars import DB_URI

conn = pg.connect(DB_URI)
q = conn.cursor()
