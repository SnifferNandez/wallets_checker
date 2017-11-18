#!/usr/bin/python
import urllib2
import json
import time

currency = {'BTC':'https://insight.bitpay.com/api/',
            'BCH':'https://cashexplorer.bitcoin.com/api/'}

# Create in wallets.txt one wallet per line
# Example using wallets from https://docs.google.com/spreadsheets/d/1xTROekDerP1TPOB3SOD_1bbQr580BPqbhF3YHdO96pw
file = open('wallets.txt', 'r') 
for wallet in file: 
  for k,v in currency.items():
    try:
      walletInfo = json.loads(urllib2.urlopen(v+'addr/'+wallet).read())
      if walletInfo['balance'] != 0:
      	info = walletInfo['addrStr'] + ' {:f}' + ' ' + k 
        print info.format(walletInfo['balance']) # Use format to avoid scientific notation
    except:
      print 'Error on ' + wallet
  time.sleep(0.05) # Limit to 20 request per second
