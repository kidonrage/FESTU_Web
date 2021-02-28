import cgi, os

form = cgi.FieldStorage() 
uploaded_image = form['uploaded_image']
file_name = os.path.basename(uploaded_image.filename)
f = open(file_name, 'wb')
f.write(uploaded_image.file.read())

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Загрузка файла</title>
    </head>
    <body>""")
print("<img src=\"http://localhost:8000/{}\" >".format(file_name))


print("""</body>
        </html>""")   
     
