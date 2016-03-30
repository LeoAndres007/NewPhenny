import urllib2
import re

# ====================
# = Real Time Quotes =
# ====================

def yahooQuote(phenny,input):
	"""Get Realtime Stock Quote From yahoo"""
#	ticker = "\"SPY\""
	symbol = input.replace(".qx ","")
	symbol = symbol.upper()
	symbol = str(symbol)
	ticker = "\""+symbol+"\""
	xml_data = yahooXML(ticker)	

	bid = BidRealtime(phenny,xml_data)
	ask = AskRealtime(phenny,xml_data)
	change = ChangeRealtime(phenny,xml_data)
	# changepct = ChangePercentRealtime(phenny,xml_data)

	phenny.say(symbol+" => "+bid+" "+ask+" "+change)
yahooQuote.rule = (['qx'], r'(.*)')	
yahooQuote.priority = 'high'

def yahooXML(ticker):
	url = "http://query.yahooapis.com/v1/public/yql?q="
	raw_ysql = "select * from yahoo.finance.quotes where symbol in ("+ticker+")"
	encoded_ysql = urllib2.quote(raw_ysql)
	yfiString = "&diagnostics=false&env=http://datatables.org/alltables.env"	
	restfulURL = url+encoded_ysql+yfiString	
	response = urllib2.urlopen(restfulURL)
	xml_data = response.read()	
	return xml_data

def BidRealtime(phenny,xml_data):
	"""BidRealtime Regex - Gets the real-time Bid Price"""
	
	re1='(<BidRealtime>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/BidRealtime>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="Bid: %s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="Bid: N/A"
	bid = float1
	return bid

def AskRealtime(phenny,xml_data):
	"""AskRealtime Regex - Gets the real-time Ask Price"""
	
	re1='(<AskRealtime>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/AskRealtime>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="Ask: %s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="Ask: N/A"
	ask = float1
	return ask

def ChangeRealtime(phenny,xml_data):
	"""ChangeRealtime Regex - Gets the real-time Change"""
	
	re1='(<ChangeRealtime>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/ChangeRealtime>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="Change: %s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="Change: N/A"
	change = float1
	return change
	
def ChangePercentRealtime(phenny,xml_data):
	"""ChangePercentRealtime Regex - Gets the real-time ChangePercentRealtime"""
	
	re1='(<ChangePercentRealtime>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/ChangePercentRealtime>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="%s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="N/A"
	changepct = float1
	return changepct
