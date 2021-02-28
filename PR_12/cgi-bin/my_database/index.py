import sqlite3

db = sqlite3.connect('database.db')
cur = db.cursor()
cur.execute("""
    CREATE TABLE if not exists user_info(
        id INTEGER PRIMARY KEY,
        name TEXT,
        password TEXT,
        occupation TEXT,
        gender TEXT,
        info TEXT,
        work TEXT);
  """)
db.commit()
cur.execute("SELECT * from user_info")
data = cur.fetchall()
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>База данных></title>
            </head>
        <body>
            <table bordercolor='black' border='1px' cellspacing='0px' style="white-space: pre-line">
                <thead>
                    <tr>
                        <th> id </th>
                        <th> Name </th>
                        <th> Password </th>
                        <th> Occupation </th>
                        <th> Gender </th>
                        <th> Info </th>
                        <th> Work </th>
                    </tr>
                <tbody>
        """)
for row in data:
    print("<tr>")
    for index, cell in enumerate(row):
        if index == 5:
            print(f"<td nowrap>{cell}</td>")
        else:
            print(f"<td>{cell}</td>")
    print("</tr>")

print("""
                </tbody>
            </table>
            <br>
            <a href='add_entry.py'> <button>Добавить запись</button> </a> <br> <br>
            <form action="update_entry.py">
                <input type='text' name="update_id" placeholder='Введите id'>
                <button>Изменить запись</button>
            </form>
            <br>
            <form action="delete_entry.py">
                <input type='text' name="delete_id" placeholder='Введите id'>
                <button>Удалить запись</button>
            </form>
        </body>
        </html>
""")