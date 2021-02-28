import cgi
import sqlite3

form = cgi.FieldStorage()

name = form.getfirst("NAME", "не задано")
password = form.getfirst("PASS", "не задано")
occupation = form.getfirst("OCCUPATION", "не задано")
gender = form.getfirst("GENDER", 'не задано')
info = form.getfirst("EDUCATION_INFO", 'не задано')
work = form.getlist("WORK")
work_entry = ""

for index, value in enumerate(work):
    if index == len(work)-1:
        work_entry += value
    else:
        work_entry += value + '\n'
db = sqlite3.connect('database.db')
cur = db.cursor()

cur.execute("""
    CREATE TABLE if not exists user_info(
        id INTEGER PRIMARY KEY,
        name TEXT,
        password integer,
        occupation TEXT,
        gender TEXT,
        info TEXT,
        work TEXT);
  """)
entry = f"""
    INSERT INTO user_info (name,password,occupation,gender,info,work) VALUES (
      '{name}',
      '{password}',
      '{occupation}',
      '{gender}',
      '{info}',
      '{work_entry}');
    """
cur.execute(entry)
db.commit()
cur.close()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
            <head>
                <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/my_database/index.py" />
            </head>
""")