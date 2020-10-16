from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import openpyxl
import time

ASXshareslist = [['AC8',0],
                 ['AGL',0],
                 ['ALK',0],
                 ['ANZ',0],
                 ['BHP',0],
                 ['CAN',0],
                 ['CBA',0],
                 ['VUK',0],
                 ['DHG',0],
                 ['ERA',0],
                 ['NEC',0],
                 ['IAG',0],
                 ['JHG',0],
                 ['MPL',0],
                 ['MPL',0],
                 ['MQG',0],
                 ['MYR',0],
                 ['NAB',0],
                 ['NHF',0],
                 ['PAN',0],
                 ['PTR',0],
                 ['RIO',0],
                 ['RNE',0],
                 ['S32',0],
                 ['S32',0],
                 ['SCP',0],
                 ['WBC',0],
                 ['WOW',0],
                 ['WTC',0],
                 ['IDZ',0],
                 ['AMP',0],
                 ['ORE',0],
                 ['ASM',0]]

driver = webdriver.Chrome('E:/Media/chromedriver_win32/chromedriver.exe')

fn = "C:\\Users\\roman\\OneDrive\\Python\\Tax.xlsx"
#fn = 'TaxTest.xlsx'

#wb = openpyxl.load_workbook(fn)
#ws = wb['Shares'] 

i=2
for x in ASXshareslist:
    i = i+1
    sShare = x[0]
    
    driver.get('https://www2.asx.com.au/markets/company/'+sShare)
    time.sleep(3)
    el = driver.find_element_by_tag_name("dd").text
    ela = el.split()
    fPrice = float(ela[0])
    
    x[1] = fPrice

    sPrice = '{:7.3f}'.format(fPrice)
    print(sShare+' : ',sPrice)
    
#    cr = ws.cell(row=i, column=2)
#    cr.value=sShare
    
#    cr = ws.cell(row=i, column=3)
#    cr.value=fPrice

#wb.save(fn)
driver.close()


