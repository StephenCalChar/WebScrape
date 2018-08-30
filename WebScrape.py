import unicodecsv
from bs4 import BeautifulSoup
import os
from selenium import webdriver


target_page = 'http://www.newlook.com/uk/womens/clothing/jackets-coats/c/uk-womens-clothing-jackets-coats?comp=NavigationBar%7Cmn%7Cwomens%7Cclothing%7Cdepartment%7Cjacketscoats#/?q=:relevance&page=3&sort=relevance&content=false'

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\Python27\geckodriver.exe')
driver.get(target_page)
html = driver.execute_script("return document.documentElement.outerHTML")

soup = BeautifulSoup(html, 'html.parser')
nameList =[]
priceList =[]

for item in soup.findAll('a', {'class': 'product-item__name'}):
    itemText = item.text.strip()
    nameList.append(itemText)

for price in soup.findAll('span', {'class': 'price'}):
    priceText = price.text.strip()
    removeCurrency = priceText[1:]
    priceList.append(removeCurrency)

print(str(len(nameList)) + ' products found.')
print(str(len(priceList)) + ' prices found.')

os.chdir('C:\Users\Steve\Desktop')

with open('scrapeNewLook.csv', 'a') as csvFile:
    writer = unicodecsv.writer(csvFile)
    count =0
    while(count < len(nameList)):
        writer.writerow([nameList[count], priceList[count]])
        count += 1

print('Document Saved.')



