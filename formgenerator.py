import pdfkit
import dropbox
parameters = {"TITLE": "My Project", "MEMBERS": "Andrew Ilyas", "DESCRIPTION": "A project description", "IMAGEURL": "hack-bg-square-3.jpg"}
f = open("judgessheet.html")
theFile = f.read()
for x in parameters:
    theFile = theFile.replace("$$" + x + "$$", parameters[x])
f2 = open("newsheet.html", "w")
f2.write(theFile)
f2.close()
pdfkit.from_file('newsheet.html', 'test.pdf')


