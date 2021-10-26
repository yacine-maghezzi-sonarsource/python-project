import requests
import time
from requests.exceptions import ConnectionError
import socket

def internet_connection_test(url):
	#url = 'https://www.google.com/' //TODO
	print(f'Attempting to connect to {url} to determine internet connection status.')
	
	try:
		print(url)
		tic = time.perf_counter()
		resp = requests.get(url, timeout = 10)
		toc = time.perf_counter()
		resp.text
		resp.status_code
		print(f'Connection to {url} was successful.')
		print(f"Resp time in {toc - tic:0.4f} seconds")
		return True
	except ConnectionError as e:
		requests.ConnectionError
		print(f'Failed to connect to {url}.')
		return False
	except:
		print(f'Failed with unparsed reason.')
		return False

def get_hostname_IP():
    hostname = input("Please enter website address(URL):")
    try:
        print (f'Hostname: {hostname}')
        print (f'IP: {socket.gethostbyname(hostname)}')
    except socket.gaierror as error:
        print (f'Invalid Hostname, error raised is {error}')
    
    internet_connection_test(hostname)

    
get_hostname_IP()

