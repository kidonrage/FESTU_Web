#!/usr/bin/env python3
import cgi
import sqlite3
form = cgi.FieldStorage()
db = sqlite3.connect('database.db')
cur = db.cursor()
entry_id = form.getfirst("update_id")

try:
    cur.execute(f"SELECT * from user_info WHERE id={entry_id}")
except sqlite3.OperationalError:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
            <html>
                <head>
                    <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/my_database/index.py" />
                </head>
    """)
    input()
entry = cur.fetchone()
if entry is None:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
                <html>
                    <head>
                        <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/my_database/index.py" />
                    </head>
        """)
    input()
name = entry[1]
password = entry[2]
occupation = entry[3]

# Да, костыль
technology_selected = ""
building_selected = ""
business_selected = ""

if occupation == "Инф. Технологии":
    technology_selected = "selected"
elif occupation == "Строительство":
    building_selected = "selected"
elif occupation == "Бизнес":
    business_selected = "selected"

gender = entry[4]

# Да, костыль 2
male_gender = ""
female_gender = ""

if gender == "Мужской":
    male_gender = "checked"
else:
    female_gender = "checked"

info = entry[5]

work = entry[6]

indifferent_checked = ""
clientele_checked = ""
documentation_checked = ""
solo_checked = ""
work_entry = work.split("\n")
for data in work_entry:
    if data == 'Всё равно':
        indifferent_checked = "checked"
    elif data == 'Работа с клиентами':
        clientele_checked = "checked"
    elif data == 'Работа с документами':
        documentation_checked = "checked"
    elif data == 'Работа в одиночку':
        solo_checked = "checked"
print("Content-type: text/html")
print()
print("<!DOCTYPE html>")
print("<html lang='en'>")
print("<head>")
print("<meta charset='UTF-8'>")
print("<title>Изменить запись</title>")
print("</head>")
print("<body>")
print("<form action='update_entry_handler.py' method='post' enctype='multipart/form-data'>")
print(f"<input name='update_id' value='{entry_id}' hidden>")
print("<h1>Заполните анкету:</h1>")
print("<p>Введите ваше ФИО:")
print(f"<input type='text' name='NAME' value='{name}' required>")
print("</p>")
print("<p>Введите пароль:")
print(f"<input type='password' name='PASS' value='{password}' required>")
print("</p>")
print("<p>Ваш род занятий:")
print("<select name='OCCUPATION'>")
print(f"<option value='Инф. Технологии' {technology_selected}> Инф. технологии</option>")
print(f"<option value='Строительство' {building_selected}> Строительство</option>")
print(f"<option value='Бизнес' {business_selected}> Бизнес</option>")
print("</select>")
print("</p>")
print("<p>Пол:")
print(f"<input type='radio' name='GENDER' value='Мужской' {male_gender}>Мужской</input>")
print(f"<input type='radio' name='GENDER' value='Женский' {female_gender}>Женский</input>")
print("</p>")
print("<p>Сведения об образовании:</p>")
print(f"<textarea name='EDUCATION_INFO' placeholder='Ваши сведения здесь' cols=45 rows=3 maxlength=50 >{info}</textarea>")
print("<p></p>")
print(f"<a>Ваши предпочтения:</a> <input name='WORK' value='Всё равно' style='margin-left:100px;' type='checkbox' {indifferent_checked}>Всё равно</input>  <br>")
print(f"<a>(один или несколько вариантов)</a> <input name='WORK' value='Работа с клиентами' style='margin-left:23px;' type='checkbox' {clientele_checked}>Работа с клиентами</input> <br>")
print(f"<input name='WORK' value='Работа с документами' style='margin-left:245px;' type='checkbox' {documentation_checked}>Работа с документами</input> <br>")
print(f"<input name='WORK' value = 'Работа в одиночку' style='margin-left:245px;' type='checkbox' {solo_checked}>Работа в одиночку</input> <br> <br>")

print("<button style='margin-left:200px;' type='reset'>Очистить</button>"
      "<button type='submit'>Подтвердить</button>")
print("</form>")
print("</body>")
print("</html>")