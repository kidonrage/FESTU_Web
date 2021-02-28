import http.cookies, os

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
login_cookie = cookie.get("login")

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Страница 4</title>
        </head>
        <body>
        <a href='page1.py'>Page 1</a>
        <a href='page2.py'>Page 2</a>
        <a href='page3.py'>Page 3</a>
        <a href='page4.py'>Page 4</a>
        """)    

if login_cookie is None:
    print("<h1>Вы не авторизованы!</h1>")
else:
    print(f"<h1>Хорошего дня, {login_cookie.value}! </h1>")
    print("""<a href='exit.py'> <button>Выход</button> </a>""")