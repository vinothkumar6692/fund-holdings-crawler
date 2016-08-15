# fund-holdings-crawler
a system that pulls fund holdings from EDGAR, given a ticker from http://www.sec.gov/edgar/searchedgar/companysearch.html
to
http://www.sec.gov/edgar/searchedgar/companysearch.html
to 
http://www.sec.gov/cgi-bin/browse-edgar?CIK=0001166559&Find=Search&owner=exclude&action=getcompany
then find 13F-HR ("13F" is the name of the report type that gives fund holdings, which is an annual or a quarterly report, so this is just another report type). Then retrieve contents from
http://www.sec.gov/Archives/edgar/data/1166559/000110465914039387/0001104659-14-039387.txt
and parse and generate tab-delimited text from xml

Requirements
=======

* BeautifulSoup


Instructions
=======

* Install the requirement "BeautifulSoup" using
```bash
$ pip install beautifulsoup4
```
* Run the app using 
```bash
$ python main.py <ticker> 
```
Here "ticker" is the command line parameter
Eg:
```bash
$ python main.py CSCO 
```
* View the fund holding information at the terminal

