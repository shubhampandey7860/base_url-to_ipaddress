# base_url-to_ipaddress
steps:
1. check ipadreess of your system:
goto command prompt type : ipconfig

or 
import socket 
hostname=socket.gethostname()  # it will give user
ipaddress=socket.gethostbyname(hostname) # it will give ipaddress


2. register it into settings.py file
ALLOW_HOST=['192.168.137.1']
3.runserver : python manage.py runserver 192.168.137.1:8000 
if u wanted to change port no you can also change

python manage.py runserver 192.168.137.1:8001 

