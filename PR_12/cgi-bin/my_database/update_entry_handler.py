import sqlite3
import cgi

db = sqlite3.connect('database.db')
cur = db.cursor()

form = cgi.FieldStorage()
update_id = form.getfirst("update_id")
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

cur.execute(f"""UPDATE user_info SET
                    name = '{name}',
                    password = '{password}',
                    occupation = '{occupation}',
                    gender = '{gender}',
                    info = '{info}',
                    work = '{work_entry}'
             WHERE id={update_id}""")
db.commit()
cur.close()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
            <head>
                <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/my_database/index.py" />
            </head>
""")