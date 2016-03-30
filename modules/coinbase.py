import requests
import re
import json

# =====================================
# = Bitcoin Spot prices from coinbase =
# =====================================

def coinbaseBTCprices(phenny,input):
	"""Get Bitcoin price info from coinbase"""
	spotURL = "https://coinbase.com/api/v1/prices/spot_rate"
	buyURL = "https://coinbase.com/api/v1/prices/buy"
	sellURL = "https://coinbase.com/api/v1/prices/sell"
	btcPriceData = []
	urls = [spotURL,buyURL,sellURL]
	for url in urls:
		data = requests.get(url, verify=True)
		dataResponse = json.loads(data.text)
		amt = float(dataResponse['amount'])
		btcPriceData.append(amt)
	btcSpotPrice = btcPriceData[0]
	btcBuyPrice = btcPriceData[1]
	btcSellPrice = btcPriceData[2]
	btcSpread = round((((btcBuyPrice-btcSellPrice)/btcSpotPrice)*100),3)
	btcPrice = "BTC => SPOT( %s ) ACTUAL( %s x %s ) SPREAD( %s%% )" % (btcSpotPrice,btcSellPrice,btcBuyPrice,btcSpread)
	phenny.say(btcPrice)
coinbaseBTCprices.rule = (['btc'], r'(.*)')	
coinbaseBTCprices.priority = 'medium'