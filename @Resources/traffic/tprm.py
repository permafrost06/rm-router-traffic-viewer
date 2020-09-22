import requests
from time import sleep
from tptools import Instance

x = Instance()

# run inifnitely
while True:
	try:
		r = x.stat()
	except:
		continue
	buffer = ""
	for item in reversed(r):
		buffer = buffer + item["mac"] + "," + item["bytes_curr"] + "\n"
	with open("data.csv", "w") as fp:
		fp.write(buffer)
		fp.close()
	sleep(5)