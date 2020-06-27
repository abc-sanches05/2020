import psycopg2

conn = psycopg2.connect(dbname='test', user='postgres',
                        password='110167', host='localhost')
cursor = conn.cursor()

cursor.execute('SELECT * FROM public.book ORDER BY book_id ASC ')
records = cursor.fetchall()
print (records)

cursor.close()
conn.close()
