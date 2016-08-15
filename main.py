import crawler
import sys

ticker = sys.argv[1]
cikFinderURL = crawler.fundHoldingCrawler(ticker)
if cikFinderURL:
	reportURL = crawler.fundHoldinglistCrawler(cikFinderURL)
	if reportURL:
		crawler.finalCrawl(reportURL) 
	else:
		print "File not found"
else:
	print "13F-H Record Not Found for "+ticker 