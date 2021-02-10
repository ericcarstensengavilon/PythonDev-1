##+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Connect and list the dir of and FTP site
#SOMETIMES THIS TIMES OUT.
import ftplib

#Open ftp connection
ftp = ftplib.FTP('ftp.jackscrib.com', 'ericftp',
'Chibby2000!')

#List the files in the current directory
print ("File List:")
files = ftp.dir()
print (files)

#Chagne  dir to the demos dir
#ftp.cwd("/demos")

#print ("File List:")
#files = ftp.dir()
#print (files)

gFile = open("Home.html", "wb")
ftp.retrbinary('RETR Home.html', gFile.write)
gFile.close()

print('FTP Closed')

#Print the readme file contents
#print ("\nReadme File Output:")
#gFile = open("readme.txt", "r")
#buff = gFile.read("GAVPOS.CSV")
#print (buff)
#gFile.close()

ftp.quit()

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Download a file
import ftplib
import sys

def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except:
        print ("Error")


ftp = ftplib.FTP("ftp.nluug.nl")
ftp.login("anonymous", "ftplib-example-1")

ftp.cwd('/pub/')         # change directory to /pub/
getFile(ftp,'README.nluug')

#FTP.delete(filename)

ftp.quit()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Upload a file

import ftplib
import os

def upload(ftp, file):
    ext = os.path.splitext(file)[1]
    if ext in (".txt", ".htm", ".html"):
        ftp.storlines("STOR " + file, open(file))
    else:
        ftp.storbinary("STOR " + file, open(file, "rb"), 1024)

ftp = ftplib.FTP("127.0.0.1")
ftp.login("username", "password")

upload(ftp, "README.nluug")
