import urllib2
import re

# ====================
# = Moving Averages  =
# ====================

def movingavgQuote(phenny,input):
	"""Get Realtime Stock Quote From yahoo"""
	# ticker = "\"SPY\""
	symbol = input.replace(".stress ","")
	symbol = symbol.upper()
	symbol = str(symbol)
	ticker = "\""+symbol+"\""
	xml_data = yahooXML(ticker)	

	lastTrade = LastTradePriceOnly(phenny,xml_data)
	stress = stressTest(phenny,lastTrade)
	
	phenny.say("\00303"+symbol+" [+10%]=> "+stress[2]+"\003")
	phenny.say("\00303"+symbol+" [+05%]=> "+stress[0]+"\003")
	phenny.say("\002"+symbol+" [Last]=> \002"+lastTrade)
	phenny.say("\00304"+symbol+" [-05%]=> "+stress[1]+"\003")
	phenny.say("\00304"+symbol+" [-10%]=> "+stress[3]+"\003")
	
movingavgQuote.rule = (['stress'], r'(.*)')	
movingavgQuote.priority = 'high'


def yahooXML(ticker):
	url = "http://query.yahooapis.com/v1/public/yql?q="
	raw_ysql = "select * from yahoo.finance.quotes where symbol in ("+ticker+")"
	encoded_ysql = urllib2.quote(raw_ysql)
	yfiString = "&diagnostics=false&env=http://datatables.org/alltables.env"	
	restfulURL = url+encoded_ysql+yfiString	
	response = urllib2.urlopen(restfulURL)
	xml_data = response.read()	
	return xml_data

def stressTest(phenny,lastTrade):
	lastTrade = float(lastTrade)
	fiveUp = (lastTrade*0.05)+lastTrade
	tenUp = (lastTrade*0.10)+lastTrade
	fiveDown = lastTrade-(lastTrade*0.05)
	tenDown = lastTrade-(lastTrade*0.10)

	fiveUp = round(fiveUp,2)
	tenUp =  round(tenUp,2)
	fiveDown = round(fiveDown,2)
	tenDown = round(tenDown,2)
	
	fiveUp = str(fiveUp)
	tenUp =  str(tenUp)
	fiveDown = str(fiveDown)
	tenDown = str(tenDown)
	
	res = [fiveUp,fiveDown,tenUp,tenDown]
	return res

def LastTradePriceOnly(phenny,xml_data):	
	re1='(<LastTradePriceOnly>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/LastTradePriceOnly>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="%s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="N/A"
	lastTrade = float1
	return lastTrade
