import sqlite3
import cgi
db = sqlite3.connect('database.db')
cur = db.cursor()

form = cgi.FieldStorage()
entry_id = form.getfirst("delete_id")
cur.execute(f"DELETE FROM user_info where id = {entry_id}")
db.commit()
cur.close()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
            <head>
                <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/my_database/index.py" />
            </head>
""")