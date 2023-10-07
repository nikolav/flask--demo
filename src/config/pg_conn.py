import psycopg2 as pg

conn = pg.connect("postgres://app:app@70.34.223.252:5544/app")
q = conn.cursor()
