import urllib2
import re

# ====================
# = Moving Averages  =
# ====================

def movingavgQuote(phenny,input):
	"""Get Realtime Stock Quote From yahoo"""
#	ticker = "\"SPY\""
	symbol = input.replace(".ma ","")
	symbol = symbol.upper()
	symbol = str(symbol)
	ticker = "\""+symbol+"\""
	xml_data = yahooXML(ticker)	

	lasttrade = LastTradePriceOnly(phenny,xml_data)
	ma50 = FiftydayMovingAverage(phenny,xml_data)
	ma200 = TwoHundreddayMovingAverage(phenny,xml_data)
	
	phenny.say(symbol+" [Last]=> "+lasttrade+" [50ma]=> "+ma50+" [200ma]=> "+ma200)
movingavgQuote.rule = (['ma'], r'(.*)')	
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

def FiftydayMovingAverage(phenny,xml_data):	
	re1='(<FiftydayMovingAverage>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/FiftydayMovingAverage>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="%s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="N/A"
	ma50 = float1
	return ma50
	
def TwoHundreddayMovingAverage(phenny,xml_data):	
	re1='(<TwoHundreddayMovingAverage>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/TwoHundreddayMovingAverage>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="%s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="N/A"
	ma200 = float1
	return ma200

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
	lasttrade = float1
	return lasttrade
