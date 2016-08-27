import requests
import re
import Queue
import random
import time
import codecs
from threading import Thread

requests.packages.urllib3.disable_warnings()


def run():
	id = 'bd7123c9c441eddfaeb4bdef'
	url = 'https://www.freecodecamp.com/challenges/comment-your-javascript-code'
	s = requests.session()
	headers = {
		'X-CSRF-Token': 'change this',
		'Referer': url,
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2837.0 Safari/537.36'
	}
	requests.utils.add_dict_to_cookiejar(
		s.cookies, 
		{
			'__cfduid': 'put',
			'_csrf': 'your',
			'access_token': 'cookie',
			'userId': 'info',
			'_gat': 'here',
			'currentChallengeId': id, #leave this one
			'connect.sid': 'here',
			'_ga': 'and here'
		}
	)
		
	r = s.get(
		url,
		verify=False,
		timeout=16,
		headers=headers
	)
	while True:
		print 'Current Challenge', id
		
		id = re.findall('common.challengeId = "(.*?)";', r.text)[0]
		name = re.findall('common.challengeName = "(.*?)";', r.text)[0]
		seed = re.findall('common.challengeSeed = \["(.*?)"\]', r.text)[0]
		
		headers['Content-Type'] = 'application/json'
		headers['X-Requested-With'] = 'XMLHttpRequest'
		headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
		
		r = s.post(
			'https://www.freecodecamp.com/completed-challenge/',
			json={
				'id': id,
				'name': name,
				'challengeType': 0,
				'solution': seed,
				'timezone': 'America/New_York'
			},
			verify=False,
			timeout=16,
			headers=headers
		)
		
		pts = re.findall('points":(.*?),', r.text)[0]
		print 'Points:', pts
		
		r = s.get(
			'https://www.freecodecamp.com/challenges/next-challenge?id={0}'.format(id),
			verify=False,
			timeout=16,
			headers=headers
		)
		print 'ID:', id
	
def main():
	run()
			
if __name__ == '__main__':
	main()
