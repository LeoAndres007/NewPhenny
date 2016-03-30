import urllib2
import re

# =================
# = Metals Prices =
# =================

def kitcoHTML():
	kitco = urllib2.urlopen('http://www.kitco.com/texten/texten.html')
	html = kitco.read()
	return html

"""
10:13 < yak> and just poll in the background. populate the db and the bot pulls the db?

basically it's a caching system with a 2minute stale timer
	stubData = ""
	if is set time-last-called:
		if time-last-called is within the past 2 minutes:
			use stub data
		else:
			get new data
			set the time-last-called
	else:
		get new data
		set the time-last-called
"""


def rtGold(phenny):
	"""Get Realtime Gold Price From Kitco"""
	html = kitcoHTML()
	
	gold_re1='(Gold)'	# Word 1
	gold_re2='(\\s+)'	# White Space 1
	gold_re3='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	gold_re4='(\\s+)'	# White Space 2
	gold_re5='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
	gold_re6='(\\s+)'	# White Space 3
	gold_re7='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 3
	gold_re8='(\\s+)'	# White Space 4
	gold_re9='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 4
	gold_re10='(%)'	# Any Single Character 1
	gold_rg = re.compile(gold_re1+gold_re2+gold_re3+gold_re4+gold_re5+gold_re6+gold_re7+gold_re8+gold_re9+gold_re10)
	gold_m = gold_rg.findall(html)
	
	goldcounter = True
	
	for gold in gold_m:
		if goldcounter:
			nygold = "NY SPOT GOLD => Bid: %s Ask: %s Change: %s %s%%" % (gold[2],gold[4],gold[6],gold[8])
			goldcounter = False
			phenny.say(nygold)
		# else:
		# 	asiagold = "ASIA/EU GOLD => Bid: %s Ask: %s Change: %s %s%%" % (gold[2],gold[4],gold[6],gold[8])
		# 	phenny.say(asiagold)

def rtSilver(phenny):
	"""Get Realtime Silver Price From Kitco"""
	html = kitcoHTML()
	
	silver_re1='(Silver)'	# Word 1
	silver_re2='(\\s+)'	# White Space 1
	silver_re3='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	silver_re4='(\\s+)'	# White Space 2
	silver_re5='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
	silver_re6='(\\s+)'	# White Space 3
	silver_re7='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 3
	silver_re8='(\\s+)'	# White Space 4
	silver_re9='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 4
	silver_re10='(%)'	# Any Single Character 1
	silver_rg = re.compile(silver_re1+silver_re2+silver_re3+silver_re4+silver_re5+silver_re6+silver_re7+silver_re8+silver_re9+silver_re10)
	silver_m = silver_rg.findall(html)
	
	silvercounter = True
	
	for silver in silver_m:
		if silvercounter:
			nysilver = "NY SPOT Silver => Bid: %s Ask: %s Change: %s %s%%" % (silver[2],silver[4],silver[6],silver[8])
			silvercounter = False
			phenny.say(nysilver)
		# else:
		# 	asiasilver = "ASIA/EU Silver => Bid: %s Ask: %s Change: %s %s%%" % (silver[2],silver[4],silver[6],silver[8])
		# 	phenny.say(asiasilver)

def rtPlatinum(phenny):
	"""Get Realtime Platinum Price From Kitco"""
	html = kitcoHTML()
	
	platinum_re1='(Platinum)'	# Word 1
	platinum_re2='(\\s+)'	# White Space 1
	platinum_re3='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	platinum_re4='(\\s+)'	# White Space 2
	platinum_re5='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
	platinum_re6='(\\s+)'	# White Space 3
	platinum_re7='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 3
	platinum_re8='(\\s+)'	# White Space 4
	platinum_re9='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 4
	platinum_re10='(%)'	# Any Single Character 1
	platinum_rg = re.compile(platinum_re1+platinum_re2+platinum_re3+platinum_re4+platinum_re5+platinum_re6+platinum_re7+platinum_re8+platinum_re9+platinum_re10)
	platinum_m = platinum_rg.findall(html)
	
	platinumcounter = True
	
	for platinum in platinum_m:
		if platinumcounter:
			nyplatinum = "NY SPOT Platinum => Bid: %s Ask: %s Change: %s %s%%" % (platinum[2],platinum[4],platinum[6],platinum[8])
			platinumcounter = False
			phenny.say(nyplatinum)
		# else:
		# 	asiaplatinum = "ASIA/EU Platinum => Bid: %s Ask: %s Change: %s %s%%" % (platinum[2],platinum[4],platinum[6],platinum[8])
		# 	phenny.say(asiaplatinum)

def rtPalladium(phenny):
	"""Get Realtime Palladium Price from Kitco"""
	html = kitcoHTML()
	
	palladium_re1='(Palladium)'	# Word 1
	palladium_re2='(\\s+)'	# White Space 1
	palladium_re3='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	palladium_re4='(\\s+)'	# White Space 2
	palladium_re5='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 2
	palladium_re6='(\\s+)'	# White Space 3
	palladium_re7='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 3
	palladium_re8='(\\s+)'	# White Space 4
	palladium_re9='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 4
	palladium_re10='(%)'	# Any Single Character 1
	palladium_rg = re.compile(palladium_re1+palladium_re2+palladium_re3+palladium_re4+palladium_re5+palladium_re6+palladium_re7+palladium_re8+palladium_re9+palladium_re10)
	palladium_m = palladium_rg.findall(html)
	
	palladiumcounter = True
	
	for palladium in palladium_m:
		if palladiumcounter:
			nypalladium = "NY SPOT Palladium => Bid: %s Ask: %s Change: %s %s%%" % (palladium[2],palladium[4],palladium[6],palladium[8])
			palladiumcounter = False
			phenny.say(nypalladium)
		# else:
		# 	asiapalladium = "ASIA/EU Palladium => Bid: %s Ask: %s Change: %s %s%%" % (palladium[2],palladium[4],palladium[6],palladium[8])
		# 	phenny.say(asiapalladium)

def rtMetals(phenny, input):
	"""Get Metals Quotes From Kitco"""
	if (input == ".rtg"):
		rtGold(phenny)
	elif (input == ".rts"):
		rtSilver(phenny)	
	elif (input == ".rtplat"):
		rtPlatinum(phenny)	
	elif (input == ".rtpal"):
		rtPalladium(phenny)
	elif (input == ".rtm"):
		rtGold(phenny)
		rtSilver(phenny)
		rtPlatinum(phenny)
		rtPalladium(phenny)
	else:
		phenny.say("quack")
rtMetals.commands = ['rtg','rts','rtplat','rtpal','rtm']
rtMetals.priority = 'medium'

# ==============
# = OIL PRICES =
# ==============
def crudeOilURL():
	"""URL for Retrieving crude oil price"""
	response = urllib2.urlopen('http://www.oil-price.net/TABLE3/gen.php?lang=en')
	html = response.read()
	return html
	
def rtCrudeOil(phenny):
	"""Get the Realtime Price of Crude Oil"""
	html = crudeOilURL()
	
	crudeOilre0='.*?'	# Non-greedy match on filler
	crudeOilre1='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1	
	crudeOilrg = re.compile(crudeOilre0+crudeOilre1,re.IGNORECASE|re.DOTALL)	
	crudeOilm = crudeOilrg.search(html)
	
	if crudeOilm:
	    oilprice=crudeOilm.group(1)
		
	# Get the change in price	
	crudeOilre1='.*?'	# Non-greedy match on filler
	crudeOilre2='(>)'	# Any Single Character 1
	crudeOilre3='(.)'	# Any Single Character 2
	crudeOilre4='(\\s+)'	# White Space 1
	crudeOilre5='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	crudeOilre6='(.)'	# Any Single Character 3
	crudeOilre7='(<)'	# Any Single Character 4	
	crudeOilrg = re.compile(crudeOilre1+crudeOilre2+crudeOilre3+crudeOilre4+crudeOilre5+crudeOilre6+crudeOilre7,re.IGNORECASE|re.DOTALL)
	crudeOilm = crudeOilrg.search(html)
	
	if crudeOilm:
		oilchange=crudeOilm.group(2)+crudeOilm.group(4)+crudeOilm.group(5)
		
	# dump the combined price + change
	oilquote = "WTI CRUDE => %s %s" % (oilprice,oilchange)
	phenny.say(oilquote)

def rtOilPrice(phenny, input):
	"""This is used for the rto single command for crude prices"""
	rtCrudeOil(phenny)
rtOilPrice.commands = ['rto']
rtOilPrice.priority = 'medium'

# =====================
# = Batch Commodities =
# =====================
def rtCommodities(phenny, input):
	"""Gets Realtime Metals and Oil"""
	if (input == ".rtcom"):
		rtGold(phenny)
		rtSilver(phenny)
		rtPlatinum(phenny)
		rtPalladium(phenny)
		rtCrudeOil(phenny)
rtCommodities.commands = ['rtcom']
rtCommodities.priority = 'medium'
