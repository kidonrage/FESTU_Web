print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Ошибка!</title>
    </head>
    <body>
    <a href='page1.py'>Page 1</a>
    <a href='page2.py'>Page 2</a>
    <a href='page3.py'>Page 3</a>
    <a href='page4.py'>Page 4</a>
    <h1>Такого пользователя не существует!</h1>
    <form method="post" action = "autorization.py">
    <p>Логин: <input type="text" name="login"> <br>
    <p>Password: <input type="password" name="password"> <br> <br>
    <input type="submit" value="Отправить"></p>
    </body>
    """)