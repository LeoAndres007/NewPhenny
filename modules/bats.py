import urllib2
import re
import json

# ====================
# = Real Time Quotes =
# ====================

def batsQuote(phenny,input):
	"""Get Realtime Stock Quote From BATS"""
	symbol = input.replace(".rq ","")
	symbol = symbol.upper()
	symbol = str(symbol)
	ticker = symbol
	json_data = batsJSON(ticker)	

	# # dumps all # json
	# phenny.say(json_data)

	data = json.loads(json_data)

	if( data['data']['company'] == 'unknown symbol'):
		phenny.say("Error or Not Traded on BATS")
	else:
		# print data['data']['trades'][0][0]
		# print data['data']['trades'][0][1]
		# print data['data']['trades'][0][2]
		# 	
		# print data['data']['bids'][0][0]
		# print data['data']['bids'][0][1]
		# print data['data']['asks'][0][0]
		# print data['data']['asks'][0][1]
		# 
		# print data['data']['volume']
		# print data['data']['company']

		symbol = data['data']['symbol']
	
		last_time = data['data']['trades'][0][0]
		last_size = data['data']['trades'][0][1]
		last_price = data['data']['trades'][0][2]
	
		bid_size = data['data']['bids'][0][0]
		bid_price = data['data']['bids'][0][1]

		ask_size = data['data']['asks'][0][0]
		ask_price = data['data']['asks'][0][1]

		volume = data['data']['volume']
		fullname = data['data']['company']

		irc_outputB = "%s( %s x %s ) Size( %s x %s ) Last( %s @ %s %s )" % (symbol,bid_price,ask_price,bid_size,ask_size,last_size,last_price,last_time)

		phenny.say(irc_outputB)
batsQuote.rule = (['rq'], r'(.*)')	
batsQuote.priority = 'medium'

def batsJSON(ticker):
	url = "http://batstrading.com/book/%s/data/" % ticker
	restfulURL = url
	response = urllib2.urlopen(restfulURL)
	json_data = response.read()
	return json_data
