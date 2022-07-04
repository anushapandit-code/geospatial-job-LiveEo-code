import sqlite3
import json

conn = None
try:
    conn = sqlite3.connect('pythonsqllite.db')

    cur = conn.cursor()

    cur.execute(""" CREATE TABLE geospatial_job ( 
                    job_id INTEGER PRIMARY KEY,
                    type TEXT CHECK(type IN ('2D', '3D')) NOT NULL DEFAULT '2D',
                    grid_file TEXT,
                    pole_file TEXT, 
                    critical_distances INTEGER CHECK(critical_distances > 0)
                   )""")
    cur.execute("INSERT INTO geospatial_job values ('')")
    # conn.commit()

except sqlite3.Error as e:
    print(e)

finally:
    if conn:
        conn.close()


