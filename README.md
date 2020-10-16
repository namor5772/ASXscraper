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

This is where the EOD share prices are loaded into when the python script is run. It is a workbook called Shares.xlsx and is assumed to have a **Shares** worksheet.
- Download it from [HERE](Shares.xlsx) into the directory **C:\Users\roman\Documents\GitHub\ASXscraper**.
- This directory might need to be created and can be changed, but you must do so consistently.
