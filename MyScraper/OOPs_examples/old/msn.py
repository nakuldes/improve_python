#This is webscraper for the MSN website.
import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.upsc.gov.in/exams-related-info/exam-notification').text
sourceText = BeautifulSoup(source, 'lxml')

#print(sourceText.prettify)
news = sourceText.findAll('table', class_='views-table cols-7')
for item in news:
    print(item.thead.tr.text)
    doeH = item.find('tr', class_='odd')
    print(doeH.text)
    #doe = item.find('th', class_='views-field views-field-field-date-commenc-ex')