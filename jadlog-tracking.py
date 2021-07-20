import sys
import time
import requests
from bs4 import BeautifulSoup

if (len(sys.argv) < 3):
    print('Arguments missing (E.g.: jadlog-tracking.py cteCode[string] time[in seconds]')
    exit()

url = 'https://www.jadlog.com.br/siteInstitucional/tracking_dev.jad?cte=' + sys.argv[1]

def getLastUpdate():
    try:
        result = requests.get(url).content
        soup = BeautifulSoup(result, 'html.parser')
        return soup.find_all('tr')[-1].find_all('td')[0].get_text()
    except:
        print('An error ocurred, will try again...')

initial_value = getLastUpdate()

print('Monitor started on:', url)

while True:
    updated_value = getLastUpdate()

    print('Last update:', updated_value)

    if initial_value != updated_value:
        initial_value = updated_value
        print('Changed! Check on', url)

    time.sleep(int(sys.argv[2]))