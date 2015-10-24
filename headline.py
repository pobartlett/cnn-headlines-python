# headline.py
# Grabs top x healines from cnn.com
# Patrick Bartlett (pojbartlett@gmail.com), 24/10/15
# Sources:
# -http://stackoverflow.com/questions/3533528/python-web-crawlers-and-getting-html-source-code
# -http://www.crummy.com/software/BeautifulSoup/bs4/doc/

import urllib2
import re
from bs4 import BeautifulSoup
import sys

no_headlines = 0	# number of headlines to pull, declared here to avoid scoping issues

# Confirm usage
if sys.argv[1] == None:
	print("Usage: headline.py <# of headlines>")
	sys.exit()
else:
	no_headlines = int(sys.argv[1])

# Raw page source from urllib2
response = urllib2.urlopen("http://cnn.com")
html_doc = response.read()

# Preparing BS for use
soup = BeautifulSoup(html_doc, 'html.parser')

# Extract headlines
# The data that we want is stored in a <span class="cd_headline-text">
headlines = soup.find_all("span", class_="cd__headline-text", limit = no_headlines)
headlines = str(headlines)

# Mold array of HTML tags into something usable. This part is quick and dirty string operations
split_headlines = headlines.split("</span>,")
regex = '<span class=\"cd__headline-text\">'	# For use with re below
result = "\n\n-----------------------------Today's Headlines-----------------------------"

for value in split_headlines:
	result += ("\n\t-"+value[len(regex)+1:])	# Append value (without extra HTML) to end string

result = result[:-len("</span>")-1]				# Remove final visible HTML attribute
result += "\n\n"
print(result)
