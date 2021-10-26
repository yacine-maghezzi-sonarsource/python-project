import requests
import time
from requests.exceptions import ConnectionError

def internet_connection_test():
	url = 'https://www.google.com/'
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

internet_connection_test()