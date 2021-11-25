import requests
import subprocess
from schedule import repeat, every, run_pending
import time

@repeat(every().day.at("10:30"))
def check_website():
    CMD = '''
    on run argv
    display notification (item 2 of argv) with title (item 1 of argv)
    end run
    '''

    def notify(title, text):
        subprocess.call(['osascript', '-e', CMD, title, text])

    URL = "https://legrandrex.cotecine.fr/reserver/F263057/?utm_campaign=le_grand_rex_paris"

    response = requests.get(URL)
    if("Spider" in str(response.content)):
        notify('LE GRAND REX', 'SPIDERMAN EST DISPO')
    else:
        notify('LE GRAND REX', 'PAS ENCORE')


while True:
    run_pending()
    time.sleep(1)
