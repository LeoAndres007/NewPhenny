import urllib2
import re

# ==============
# = Dividends  =
# ==============

def dividendQuote(phenny,input):
	"""Get Realtime Stock Quote From yahoo"""
#	ticker = "\"SPY\""
	symbol = input.replace(".dx ","")
	symbol = symbol.upper()
	symbol = str(symbol)
	ticker = "\""+symbol+"\""
	xml_data = yahooXML(ticker)	

	dividend = DividendShare(phenny,xml_data)
	dividendyield = DividendYield(phenny,xml_data)
	# exdividend = ExDividendDate(phenny,xml_data)
	# dividendpaydate = DividendPayDate(phenny,xml_data)

	if (dividend != "N/A" and dividendyield != "N/A"):
		squawk = "%s pays a dividend of $%s which yields %s%%" % (symbol,dividend,dividendyield)
		phenny.say(squawk)
	# elif (dividend == "N/A" and dividendyield != "N/A"):
	# 	squawk = "%s yields %s%%" % (symbol,dividendyield)
	# 	phenny.say(squawk)
	# elif (dividend == "N/A" and dividendyield == "N/A"):
	# 	squawk = "%s pays a dividend of $%s" % (symbol,dividend)
	# 	phenny.say(squawk)
	else:
		phenny.say("N/A or No Dividend")
				
	# if (exdividend != "N/A" and dividendpaydate != "N/A"):
	# 	squawk2 = "%s went ex-dividend on %s with a pay date on %s" % (symbol,exdividend,dividendpaydate)
	# 	phenny.say(squawk2)
	# elif (exdividend == "N/A" and dividendpaydate != "N/A"):
	# 	squawk2 = "%s had a pay date on %s" % (symbol,dividendpaydate)
	# 	phenny.say(squawk2)
	# elif (exdividend != "N/A" and dividendpaydate == "N/A"):
	# 	squawk2 = "%s went ex-dividend on %s" % (symbol,exdividend,dividendpaydate)
	# 	phenny.say(squawk2)
	# else:
	# 	pass

dividendQuote.rule = (['dx'], r'(.*)')	
dividendQuote.priority = 'high'

def yahooXML(ticker):
	url = "http://query.yahooapis.com/v1/public/yql?q="
	raw_ysql = "select * from yahoo.finance.quotes where symbol in ("+ticker+")"
	encoded_ysql = urllib2.quote(raw_ysql)
	yfiString = "&diagnostics=false&env=http://datatables.org/alltables.env"	
	restfulURL = url+encoded_ysql+yfiString	
	response = urllib2.urlopen(restfulURL)
	xml_data = response.read()	
	return xml_data

def DividendShare(phenny,xml_data):	
	re1='(<DividendShare>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/DividendShare>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="%s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="N/A"
	dividendshare = float1
	return dividendshare

def DividendYield(phenny,xml_data):	
	re1='(<DividendYield>)'	# Tag 1
	re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1
	re3='(<\\/DividendYield>)'	# Tag 2
	
	rg = re.compile(re1+re2+re3)
	m = rg.search(xml_data)
	if m:
	    tag1=m.group(1)
	    float1="%s" % m.group(2)
	    tag2=m.group(3)
	else:
	    float1="N/A"
	dividendyield = float1
	return dividendyield

def ExDividendDate(phenny,xml_data):	
	re1='(<ExDividendDate>)'	# Tag 1
	re2='((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))'	# Month 1
	re3='( )'	# White Space 1
	re4='(\\d+)'	# Integer Number 1
	re5='(<\\/ExDividendDate>)'	# Tag 2

	rg = re.compile(re1+re2+re3+re4+re5)
	m = rg.search(xml_data)
	if m:
	    month="%s" % m.group(2)
	    day="%s" % m.group(4)
	    date = "%s %s" % (month,day)
	else:
	    date="N/A"
	exdividend = date
	return exdividend

def DividendPayDate(phenny,xml_data):	
	re1='(<DividendPayDate>)'	# Tag 1
	re2='((?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Sept|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?))'	# Month 1
	re3='( )'	# White Space 1
	re4='(\\d+)'	# Integer Number 1
	re5='(<\\/DividendPayDate>)'	# Tag 2

	rg = re.compile(re1+re2+re3+re4+re5)
	m = rg.search(xml_data)
	if m:
	    month="%s" % m.group(2)
	    day="%s" % m.group(4)
	    date = "%s %s" % (month,day)
	else:
	    date="N/A"
	dividendpaydate = date
	return dividendpaydate



