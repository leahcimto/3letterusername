# something im working on


import requests

import time


apirequest = (input('username?'))
print("\nPlease wait. This may take up to 5 seconds to prevent spamming the api.\n")
time.sleep(6)
response = requests.get(f'https://api.scratch.mit.edu/users/{apirequest}')

if response.status_code == 200:
  print(f"{apirequest} exists")
if response.status_code == 404:
  print(f"{apirequest} does not exist")
print('\n')
