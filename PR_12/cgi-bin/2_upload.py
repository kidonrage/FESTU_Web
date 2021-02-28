print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Загрузка изображения</title>
        </head>
        <body>""")

print("""<form enctype="multipart/form-data" method="post" action = "2_viewer.py">
   <input type='file' id='image_upload' name='uploaded_image' accept='.jpg, .jpeg, .png'><br> <br>
   <input type="submit" value="Отправить"></p>""")        

print("""</body>
        </html>""")
