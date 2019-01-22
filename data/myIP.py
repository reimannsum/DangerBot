from requests import get
from mailservice import send
ip = get('https://api.ipify.org').text
file = open('myIP','r')
currentIP = file.readline().strip()
file.close()
if not currentIP == ip:
	# do email ne
	file.open('myIP','w')
	file.write(ip)
	file.close()