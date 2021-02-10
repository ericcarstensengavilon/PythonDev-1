from ftplib import FTP
#from datetime import date
#from datetime import timedelta
#import time
import shutil

ftps = FTP('ftp.gavilon.com')  # connect to host, default port
ftps.login(user='Q001022',passwd='Fo2wMQO0e')

interval = .5  # in seconds.  Can be a decimal

print("Checking StoneX FTP site for files...")

ftps.pwd()

print("listing here:")
#ftps.retrlines('LIST')
# Get All Files
files = ftps.nlst()
fn = 0
for file in files:
#    time.sleep(interval)
    try:
        print("Found..." + file)
        fn += 1
        #ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
    except:
        print ("Error: File could not be downloaded or found " + file)

if fn > 0:
    print(str(fn) + " files found")
    
ftps.quit()

