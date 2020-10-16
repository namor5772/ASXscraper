from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import time

# List of ASX codes for which EOD sellement prices will be obtained
ASXshareslist = [['AC8',0],['AGL',0],['ALK',0],['ANZ',0],['BHP',0],
                 ['CAN',0],['CBA',0],['VUK',0],['DHG',0],['ERA',0],
                 ['NEC',0],['IAG',0],['JHG',0],['MPL',0],['MQG',0],
                 ['MYR',0],['NAB',0],['NHF',0],['PAN',0],['PTR',0],
                 ['RIO',0],['RNE',0],['S32',0],['SCP',0],['WBC',0],
                 ['WOW',0],['WTC',0],['IDZ',0],['AMP',0],['ORE',0],
                 ['ASM',0]]

# location of Chrome driver. Adjust as necessary.
driver = webdriver.Chrome('C:\\Users\\roman\\Documents\\GitHub\\ASXscraper\\chromedriver.exe')

# location of Excel workbook where price data is saved. Adjust as necessary.
fn = "C:\\Users\\roman\\Documents\\GitHub\\ASXscraper\\Shares.xlsx"

# open above workbook so that data can be added
wb = openpyxl.load_workbook(fn)

# Worksheet assumed to exist in Above Excel workbook
ws = wb['Shares'] 

i=2
for x in ASXshareslist:
    i = i+1

    # ASX share code being considered
    sShare = x[0]

    # loops through ASX web pages that contain EOD share prices   
    driver.get('https://www2.asx.com.au/markets/company/'+sShare)
    time.sleep(3) # need delay to alow time for web page to fully load
    el = driver.find_element_by_tag_name("dd").text
    ela = el.split()
    
    # ASX EOD share price is collected and formatted
    fPrice = float(ela[0])
    x[1] = fPrice
    sPrice = '{:7.3f}'.format(fPrice)
    print(sShare+' : ',sPrice)

    # populating Excel workbook cells for considered share
    cr = ws.cell(row=i, column=2)
    cr.value=sShare
    cr = ws.cell(row=i, column=3)
    cr.value=fPrice

# Save Excel workbook
wb.save(fn)

# close interface to Chrome browser
driver.close()


