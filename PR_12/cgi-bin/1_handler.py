#!/usr/bin/env python3
import cgi

form = cgi.FieldStorage()
name = form.getfirst("NAME", "не задано")
password = form.getfirst("PASS", "не задано")
occupation = form.getfirst("OCCUPATION", "не задано")
gender = form.getfirst("GENDER", 'не задано')

info = form.getfirst("EDUCATION_INFO", 'не задано')
work = form.getlist("WORK")


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных</title>
        </head>
        <body>""")

print("<h1>Обработка данных формы!</h1>")
print(f"<p>ФИО: {name}</p>")
print(f"<p>Пароль: {password}</p>")
print(f"<p>Род занятий: {occupation}</p>")
print(f"<p>Пол: {gender}</p>")
print(f"<p>Сведения об образовании: {info}</p>")
print(f"<p>Предпочтения: {work}</p>")
print("""</body>
        </html>""")