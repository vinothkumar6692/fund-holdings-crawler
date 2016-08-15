from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib
import sys
import display_funds


'''
The function getCIKFromTicker is used to retrieve the CIK a specific company
@param targetTicker
		Ticker for the target company. Eg: ibm
@return targetCIK
		CIK no for the target company.	
'''
def getCIKFromTicker(targetTicker):

	targetURL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK="+targetTicker+"&Find=Search&owner=exclude&action=getcompany&output=atom"
	reader = urllib.urlopen(targetURL).read()
	content = BeautifulSoup(reader, "html.parser")
	cik = content.select('cik')
	targetCIK = cik[0].getText()
	return targetCIK

'''
The function fundHoldingCrawler is used to retrieve the contents of the http://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&Find=Search&owner=exclude&action=getcompany
and parse its content to find the 13F-HR report link.
@param targetTicker
		Ticker for the target company. Eg: ibm
@return links[0]
		Hyperlink to the 13F-HR report page .
'''
def fundHoldingCrawler(targetTicker):
	links = []
	targetCIK  = getCIKFromTicker(targetTicker)
	targetURL = "https://www.sec.gov/cgi-bin/browse-edgar?CIK="+targetCIK+"&Find=Search&owner=exclude&action=getcompany"
	reader = urllib.urlopen(targetURL).read()
	content = BeautifulSoup(reader, "html.parser")
	tr = content.find('table', {'class': 'tableFile2'}).find_all("tr")
	for row in tr:
		try:
			cells = row.findAll("td")
			rn = cells[0].get_text()
			if rn == '13F-HR':
				links.append(cells[1].find('a').get('href'))
		except:
			pass
	if len(links) > 0:
		return links[0]
	else:
		return None

'''
The function fundHoldinglistCrawler is used to crawl the 13F-HR report page and find the hyperlink to the page 
where the fund holding information is stored in a txt file.
@param reportURL
       URL to the 13F-HR report page
@return
       Hyperlink to the page where the txt file is stored
'''
def fundHoldinglistCrawler(reportURL):
	targetURL = "http://www.sec.gov"+reportURL
	reader = urllib.urlopen(targetURL).read()
	content = BeautifulSoup(reader, "html.parser")
	tr = content.find('table', {'class': 'tableFile'})

	for row in tr:
		try:
			cells = row.findAll("td")
			rn = cells[1].get_text()
			if rn == 'Complete submission text file':
				return cells[2].find('a').get('href')
		except:
			pass
	return None

'''
The function finalCrawl is used to crawl the final page where the fund holding information is stored. 
Uses the functions from the 'display_funds' module to generate the output at the terminal.
@param finalURL
       URL to the page where the information is stored in an XML
'''
def finalCrawl(finalURL):
	targetURL = "https://www.sec.gov/"+finalURL
	reader = urllib.urlopen(targetURL).read()
	content = BeautifulSoup(reader, "lxml-xml")
	display_funds.headerInfoDisplay(content)
	display_funds.infoTableDisplay(content)






		
	


