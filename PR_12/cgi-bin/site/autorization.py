import cgi
form = cgi.FieldStorage()
user_login = form.getvalue('login')
user_password = form.getvalue('password')
users_list = {'user1': 'password1', 'user2': 'password2', 'user3': 'password3', 'admin': 'admin'}
login_failed = True
for user in users_list.keys():
    if user_login == user and user_password == users_list[user]:
        print(f"Set-cookie: login={user_login};")
        print("Content-type: text/html\n")
        print("""<!DOCTYPE HTML>
                <head>
                    <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/site/page1.py" />
                </head>
        """)
        login_failed = False
if login_failed:
    print("Content-type: text/html\n")
    print("""<!DOCTYPE HTML>
<head>
    <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/site/autorization_failed.py" />
</head>
""")
