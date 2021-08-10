import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS RecordONE (song_name REAL, time TEXT)')


conn.commit()
c.close()
conn.close()
