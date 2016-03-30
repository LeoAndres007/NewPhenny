from BeautifulSoup import BeautifulSoup
import tinyurl
import urllib2
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

# =======================
# = Bloomberg Headlines =
# =======================

def bbghour(phenny,input):
	url="http://www.bloomberg.com/quickview/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())

	headlines=soup.findAll('li',{'class':'quick_view_bar'})

	newsmatrix = []

	for x in headlines:
		if x.find('a',{'data-type':'Story'}):
			# get the timestamp
			timestamp = x.find('p',{'class':'timestamp'})

			# if the timestamp has a string
			if timestamp.string:
				timestamp = timestamp.string
				tmin = timestamp[:2]
				tmin = int(tmin)

				# if the timestamp has minutes ago in the string
				if ('minute ago' in timestamp) or ('minutes ago' in timestamp):

					# format the headline
					headline = x.find('a').string
					link = x.find('a')['href']
					link = "http://www.bloomberg.com%s" % link
					link = tinyurl.create_one(link)
					snippet = "%s - %s (%s)" % (headline,timestamp,link)
					derp = [float(tmin),snippet]
					newsmatrix.append(derp)

	newsmatrix.sort(key=lambda x: x[0])

	for x in newsmatrix:
		phenny.say(x[1])

bbghour.commands = ['bbg']
bbghour.priority = 'medium'


def bbgmore(phenny,input):
	url="http://www.bloomberg.com/quickview/"
	page=urllib2.urlopen(url)
	soup = BeautifulSoup(page.read())

	headlines=soup.findAll('li',{'class':'quick_view_bar'})

	newsmatrix = []

	for x in headlines:
		if x.find('a',{'data-type':'Story'}):
			# get the timestamp
			timestamp = x.find('p',{'class':'timestamp'})

			# if the timestamp has a string
			if timestamp.string:
				timestamp = timestamp.string
				tmin = timestamp[:2]
				tmin = int(tmin)

				# if the timestamp has minutes ago in the string
				if ('hour ago' in timestamp) or ('hours ago' in timestamp):

					# format the headline
					headline = x.find('a').string
					link = x.find('a')['href']
					link = "http://www.bloomberg.com%s" % link
					link = tinyurl.create_one(link)
					snippet = "%s - %s (%s)" % (headline,timestamp,link)
					derp = [float(tmin),snippet]
					newsmatrix.append(derp)

	newsmatrix.sort(key=lambda x: x[0])

	for x in newsmatrix:
		phenny.say(x[1])


bbgmore.commands = ['bbgmore']
bbgmore.priority = 'medium'
