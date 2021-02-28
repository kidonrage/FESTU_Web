print("Set-cookie: login = Exit; Expires=Wed, 30 Aug 2000 00:00:00 GMT")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <head>
            <meta http-equiv="refresh" content="0;URL=http://localhost:8000/cgi-bin/site/page1.py" />
            <title>stub</title>
        </head> 
""")
