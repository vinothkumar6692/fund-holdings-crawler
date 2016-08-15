import xml.etree.ElementTree as ET
import csv
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib
import sys

'''
Module to generate tab separated output from the target XML.
'''
def headerInfoDisplay(soup):
	#Parse headerData from 1st XML
	root = soup.find('XML').find('headerData')
	if root.submissionType:
		print 'submissionType\t{}'.format(root.submissionType.string)
	if root.filerInfo:
		child = root.filerInfo
		if child.liveTestFlag:
			print 'liveTestFlag\t{}'.format(child.liveTestFlag.string)
		if child.filer.credentials:
			print 'filter'
			print '\tcredentials'
			print '\t\tcik{}\tccc\t{}'.format(child.filer.credentials.cik.string,child.filer.credentials.ccc.string)
		if child.periodOfReport:
			print 'periodOfReport\t{}'.format(child.periodOfReport.string)

	formData = soup.find('XML').find('formData')
	if formData.coverPage:
		child = formData.coverPage
		print 'formData'
		if child.reportCalendarOrQuarter:
			print '\treportCalendarOrQuarter\t{}'.format(child.reportCalendarOrQuarter.string)
		if child.isAmendment:
			print '\tisAmendment\t{}'.format(child.isAmendment.string)		
		if child.filingManager:
			print '\tfilingManager'

			if child.filingManager.find('name'):
				print '\t\tname\t{}'.format(child.filingManager.find('name').getText())
			if child.filingManager.address:
				address = child.filingManager.address
				street,city,state,zipcode=None,None,None,None
				street,city,state,zipcode= address.street1.string,address.city.string,address.stateOrCountry.string,address.zipCode.string
				print '\t\taddress\t{}\t{}\t{}\t{}'.format(street,city,state,zipcode)
			#print child.filingManager
		if child.reportType:
			print '\treportType\t{}'.format(child.reportType.string)
		if child.form13FFileNumber:
			print '\tform13FFileNumber\t{}'.format(child.form13FFileNumber.string)
		if child.provideInfoForInstruction5:
			print '\tprovideInfoForInstruction5\t{}'.format(child.provideInfoForInstruction5.string)				

	if formData.signatureBlock:
		child = formData.signatureBlock
		print 'signatureBlock'
		if child.find('name'):
			print '\tname\t{}'.format(child.find('name').getText())
		if child.title:
			print '\ttitle\t{}'.format(child.title.string)
		if child.phone:
			print '\tphone\t{}'.format(child.phone.string)	
		if child.signature:
			print '\tsignature\t{}'.format(child.signature.string)
		if child.city:
			print '\tcity\t{}'.format(child.city.string)	
		if child.stateOrCountry:
			print '\tstateOrCountry\t{}'.format(child.stateOrCountry.string)	
		if child.signatureDate:
			print '\tsignatureDate\t{}'.format(child.signatureDate.string)						


	if formData.summaryPage:
		child = formData.summaryPage	
		print 'summaryPage'
		if child.otherIncludedManagersCount:
			print '\totherIncludedManagersCount\t{}'.format(child.otherIncludedManagersCount.string)
		if child.tableEntryTotal:
			print '\ttableEntryTotal\t{}'.format(child.tableEntryTotal.string)
		if child.tableValueTotal:
			print '\ttableValueTotal\t{}'.format(child.tableValueTotal.string)	
		if child.isConfidentialOmitted:
			print '\tisConfidentialOmitted\t{}'.format(child.isConfidentialOmitted.string)				



def infoTableDisplay(soup):
	try:
		root = soup.find_all('XML')[1].find('informationTable').find_all('infoTable')
		print 'informationTable'
		for child in root:
			print 'infoTable'
			if child.nameOfIssuer:
				print '\tnameOfIssuer\t{}'.format(child.nameOfIssuer.string)	
			if child.titleOfClass:
				print '\ttitleOfClass\t{}'.format(child.titleOfClass.string)	
			if child.cusip:
				print '\tcusip\t{}'.format(child.cusip.string)
			if child.value:
				print '\tvalue\t{}'.format(child.value.string)		

			if child.shrsOrPrnAmt:
				print '\tshrsOrPrnAmt'
				nested = child.shrsOrPrnAmt
				if nested.sshPrnamt:
					print '\t\tsshPrnamt\t{}'.format(nested.sshPrnamt.string)	
				if nested.sshPrnamtType:
					print '\t\tsshPrnamtType\t{}'.format(nested.sshPrnamtType.string)	
			
			if child.votingAuthority:
				print '\tvotingAuthority'
				nested = child.votingAuthority
				if nested.Sole:
					print '\t\tSole\t{}'.format(nested.Sole.string)	
				if nested.Shared:
					print '\t\tShared\t{}'.format(nested.Shared.string)				
				if nested.None:
					print '\t\tNone\t{}'.format(nested.None.string)	

			if child.investmentDiscretion:
				print '\tinvestmentDiscretion\t{}'.format(child.investmentDiscretion.string)	

			print ' '			

	except:
		pass				


