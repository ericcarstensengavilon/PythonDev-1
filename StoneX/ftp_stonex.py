from ftplib import FTP
from datetime import date
from datetime import timedelta
#import time
import shutil

ftps = FTP('ftp.gavilon.com')  # connect to host, default port
ftps.login(user='Q001022',passwd='Fo2wMQO0e')

interval = .5  # in seconds.  Can be a decimal

# Get today's date 
today = date.today() 
print("Today is: ", today) 
  
# Yesterday date 
yesterday = today - timedelta(days = 1) 
print("Yesterday was: ", yesterday)

stonex_date = yesterday.strftime("%Y%m%d")
print("StoneX's Date = ", stonex_date)

file = "GAVPOS_" + stonex_date + "_EOD.csv"

print("File we're looking for is: ", file)

ftps.pwd()

print("listing here:")
#ftps.retrlines('LIST')
# Get All Files
files = ftps.nlst()

for file in files:
#    time.sleep(interval)
    try:
        print("Downloading..." + file)
        ftps.retrbinary("RETR " + file ,open(file, 'wb').write)
    except:
        print ("Error: File could not be downloaded " + file)

    print('Moving ' + file + ' to \\tedfil01\InformaticaDEV\Process\Position\StoneX')
    shutil.move(file, '\\\\tedfil01\\InformaticaDEV\\Process\\Position\\StoneX\\' + file)
    #ftp.delete(file)
    #ftp.delete('MONEYFILE.csv')
    print("File Moved")   
    
ftps.quit()

