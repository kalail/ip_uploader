# Imports
import requests
import time
import logging


# Settings
get_ip_url = 'http://www.myexternalip.com/raw'
# update_ip_url = 'http://dcdashboard.herokuapp.com/raw'
update_ip_url = 'http://0.0.0.0:8000/update_ip'

logging.basicConfig(filename='log.txt',level=logging.DEBUG)


# Methods
def get_ip():
	r = requests.get(get_ip_url)
	ip = r.text[:]
	return ip

def update_ip(ip):
	data = {'ip': ip}
	requests.post(update_ip_url, data)


# Main
if __name__ == '__main__':
	logging.info('Starting IP updater')
	# Run infinitely
	while True:
		try:
			# Get ip
			logging.info('Sending request to find external IP.')
			ip = get_ip()[:-1]
			logging.info('Recieved IP: ' + ip)

			# Update ip on server
			logging.info('Updating IP on dashboard.')
			update_ip(ip)
			logging.info('Updated IP.')

		except requests.exceptions.RequestException:
			logging.error('Could not send request.')

		# Wait 30 seconds
		logging.info('Sleeping for 30 seconds')
		time.sleep(30)