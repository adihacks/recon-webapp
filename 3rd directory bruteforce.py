directory bruteforce

#!/usr/bin/python
import requests
import io
from fake_useragent import UserAgent
ua = UserAgent()
user_agent = ua.random
host='http://192.168.90.27/'
filepath = 'wordlist.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:
        combined = host+line.strip()
        r = requests.get(combined, headers={'User-Agent': user_agent})
        if r.status_code == 200:
            print line.strip(),'\n',r
        line = fp.readline()
