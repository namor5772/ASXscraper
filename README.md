# ASX scraper

Basic python program that uses Selenium to automatically collect EOD settlement prices for a list of shares. This is a a rewrite of previous code that does not work due to "upgrades" to the ASX websites that previously worked with Beautiful Soup.

## Assumptions

 - We use a Windows 10 PC with internet
 - Google Chrome browser is installed
 - MS Excel is installed

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

- Open the command terminal by running the Command Prompt App. You can find it by typing **Command Prompt** in the Search bar
- Run
  ``` 
  python -m pip install selenium
  ```
- If not already installed you should see something like this in the terminal window
![alt text](images/SeleniumInstall.png "Selenium Install")

## Install the openpyxl Python module.
