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
