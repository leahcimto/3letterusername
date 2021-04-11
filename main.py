import itertools

import requests

import time
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

keywords = [''.join(i) for i in itertools.product(alphabets, repeat = 3)]
good = '<Response [404]>'
for alpha1 in alphabets:
    for alpha2 in alphabets:
        for alpha3 in alphabets:
            keywords.append(alpha1+alpha2+alpha3)
            apirequest = alpha1+alpha2+alpha3
            # response = requests.get(f'https://api.scratch.mit.edu/users/{apirequest}')
            if response == good:
                print(response, apirequest)
            time.sleep(5) # Delay for 5 seconds.