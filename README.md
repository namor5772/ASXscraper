# ASX scraper

Basic python program that uses Selenium to automatically collect EOD settlement prices for a list of shares. This is a a rewrite of previous code that does not work due to "upgrades" to the ASX websites that previously worked with Beautiful Soup.

## Assumptions

 - We use a Windows 10 PC with internet
 - The Google Chrome browser is installed
 - Microsoft Excel is installed
 - The **C:\Users\roman\Documents\GitHub\ASXscraper** will be the working directory. It is arbitrary but if a different one is used it must be changed consistently.

## Download Python with IDLE and pip

- Go to https://www.python.org/downloads/windows/
- For the latest Stable Releases download: **Windows x86-64 executable installer** or **Windows x86 executable installer** as appropriate
- Run the installer with the default directory path and both options ticked:

  ![alt text](images/PythonInstall.png "Python Install")
- Create Desktop Shortcut for running IDLE
  - There are several ways of doing this. The easiest being to drag the IDLE icon from the start menu (Left mouse button click on Window Icon on the Task Bar) to the desktop:

    ![alt text](images/PythonInstall2.png "Python Desktop Shortcut")
  - Once run select **File=>Path Browser**. This lets you see where everything is located.

## Install the Selenium Python module

This enables python to interact with websites.

- Open the command terminal by running the Command Prompt App. You can find it by typing **Command Prompt** in the Search bar. Now type the following and press the Enter key:
  ``` 
  python -m pip install selenium
  ```
- If not already installed you should see something like this in the terminal window.

  ![alt text](images/SeleniumInstall.png "Selenium Install")
- The directory from which you run the above is irrelevant.
- You can confirm installation by looking for Selenium* directories in
**C:\Users\roman\AppData\Local\Programs\Python\Python39\Lib\site-packages**

  ![alt text](images/SeleniumInstall2.png "Selenium Install2")

## Install the openpyxl Python module

This enables python to interact with Excel workbooks.

- In command terminal run
  ``` 
  python -m pip install openpyxl
  ```
- If not already installed you should see something like this in the terminal window

  ![alt text](images/OpenpyxlInstall.png "Selenium Install")
- You can confirm installation analagously to Selenium above.

## Install the Chrome Driver

This an interface used by Selenium to control the Chrome browser. You need a version consistent with your version of Chrome.

- Find out which version of the Chrome browser you are using.
  - In the browser window click the three-dot icon in the top-right corner and select **Help=>About Google Chrome**

    ![alt text](images/Chrome.png "Chrome version")
  - The first two numbers are relevant (in our case 86 above)

- Go to https://chromedriver.chromium.org/downloads
  - Click on the link to the relevant driver version. In our case: **ChromeDriver 86.0.4240.22**
  https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/
  - Download **chromedriver_win32.zip**
  - Extract this zip file into the directory **C:\Users\roman\Documents\GitHub\ASXscraper**. This might need to be created and can be changed, but you must do so consistently.

    ![alt text](images/Chrome2.png "Selenium Install")

  - NOTE: If the version has not changed you can download it from [HERE](chromedriver.exe)

## Get the Excel workbook

This is where the EOD share prices are loaded into when the python script is run. It is a workbook called **Shares.xlsx**

- Download it from [HERE](Shares.xlsx) into the directory **C:\Users\roman\Documents\GitHub\ASXscraper**.
  - You can create it yourself as long as it has a **Shares** worksheet.
- This directory might need to be created and can be changed, but you must do so consistently.

## Get the Python Script

This is the Python script that you run to download share prices. It assumes you have performed all the above installations. it is called **ASX_Selenium_scraper.py**

```python
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

```

- Download it from [HERE](ASX_Selenium_scraper.py) into the directory **C:\Users\roman\Documents\GitHub\ASXscraper**.
- This directory might need to be created and can be changed, but you must do so consistently.
- At this point you should be able to succesfully run it from IDLE 