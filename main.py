import psycopg2 as pg2
conn = pg2.connect(database = 'dvdrental', user = 'postgres', password = 'password')

cur = conn.cursor()
cur.execute('SELECT * FROM payment')

cur.fetchone()
data =cur.fetchmany(10)
#cur.fetchall() If you wanna fetch all of them

conn.close()

##


