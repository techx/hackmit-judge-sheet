import pdfkit
import dropbox
import pandas as pd


allsubmissions = pd.read_csv('topten.csv')
fx = open('topten.txt')
topten = [x[:-1] for x in fx.readlines()]
print topten
toptensubs = allsubmissions[(allsubmissions['#'].isin(topten))]
# topten = []
# for thisline in fx.readlines():
#     line = thisline.split(" // ")
#     title = line[0]
#     members = line[1]
#     description = line[2]
#     tablenum = line[3]
#     imageurl = "Hack MIT - " + tablenum + "-" + title + ".jpg"
#     topten += [{"TITLE": title, "MEMBERS": members, "DESCRIPTION": description,  "IMAGEURL": imageurl}]

app_key = 'm5n5yem1mn8cizq'
app_secret = 'v19hdvge5wujisq'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()
access_token, user_id = flow.finish(code)
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

f = open("newsheet.html", "w")
f.write("")
f.close()
#
for index, row in toptensubs.iterrows():
    f = open("judgessheet.html")
    theFile = f.read()
    faf, metadata = client.get_file_and_metadata('/File requests/HackMIT Photo Submissions/Hack MIT - ' + str(row["Table Number"]) + "-" + row["Project Title"] + ".jpg")

    out = open(str(row["Table Number"]) + row["Project Title"] + ".jpg", 'wb')
    out.write(faf.read())
    out.close()
    theFile = theFile.replace("$$TITLE$$", row["Project Title"])
    theFile = theFile.replace("$$MEMBERS$$", row["List of team members"])
    theFile = theFile.replace("$$DESCRIPTION$$", row["List of team members"])
    theFile = theFile.replace("$$IMAGEURL$$", str(row["Table Number"]) + row["Project Title"] + ".jpg")
    f2 = open("newsheet.html", "a")
    f2.write(theFile)
    f2.close()
pdfkit.from_file('newsheet.html', 'test.pdf')
