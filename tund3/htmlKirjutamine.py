#file = open("näide.html", "x")
file = open("näide.html", "w")

top = """<html>
<head></head>
<body><p>"""
tekst = "Tere maailm"
bottom = """</p></body>
</html>"""
file.write(top)
file.write(tekst)
file.write(bottom)
file.close()