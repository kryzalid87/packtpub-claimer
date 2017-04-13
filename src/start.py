import os
import schedule
import time

def do_dailly():
	os.system("scrapy runspider claim.py")
	
os.system("scrapy runspider claim.py")
schedule.every().day.at("05:00").do(do_dailly)

while True:
	schedule.run_pending()
	time.sleep(60)
