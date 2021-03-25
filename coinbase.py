import requests
import json
import time
from subprocess import run,Popen,call

#import telegram-send
#telegram_send.send(messages=["Wow that was easy!"])

print("""

SUPPORTED COINS :

(CGLD), AAVE, ADA, ALGO, ANKR, ATOM,
BAL, BAND, BAT, BCH, BNT, BSV, BTC,
Celo, COMP, CRV, CVC,
DAI, DASH, DNT,
EOS, ETC, ETH,
FIL,
GNT, GRT,
KNC,
LINK, LOOM, LRC, LTC,
MANA, MATIC, MKR, NMR,
NU,
OMG, OXT,
REN, REP,
SKL, SNX, STORJ, SUSHI,
UMA, UNI, USDC,
WBTC,
XLM, XRP, XTZ,
YFI,
ZEC, ZRX

""" )


currName =str(input('CURRENCY   :\t')).strip()
target = float(input('TARGET PRICE:\t'))
print('interval must be bigger than 3 seconds')
interval = int(input('SET YOUR INTERVAL (seconds) :\t'))

while True:
    resp = requests.get(f'https://api.coinbase.com/v2/prices/{currName}-USD/spot')
    #data = json.dumps(resp.json())
    data = resp.json()

    currency = data['data']['base']
    price = data['data']['amount']
    timestamp = time.ctime()

    print('='*50)
    print(f'Time        : {timestamp}')
    print(f'Currency    : {currency}')
    print(f'Price       : {price} $')

    if float(price) > target:
        print('Sell')
        #telegram_send.send(messages=["You Can Sell Now!"])
        command = ['telegram-send',f'Target price reached : {target} . You Can Sell Your {currName} Right Now!']
        run(command)
        break

    else:
        diff = round(target - float(price) , 2)
        diffPercent = round(100*(1 - (float(price) / target)) , 2)
        print('Status      : Hold')
        print(f'Diff        : -{diff}')
        print(f'Diff Percent: -%{diffPercent}')
        #telegram_send.send(messages=[f"Hold Your {currName}!"])
        #command = ['telegram-send',f'Hold your {currName}']
        #run(command)
        pass

    print('='*50)
    time.sleep(interval)
