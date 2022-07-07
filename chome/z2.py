import undetected_chromedriver as uc
from selenium import webdriver

options = uc.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
# e.g. Chrome path in Mac =/Users/x/Library/xx/Chrome/Default/
options.add_argument( "--user-data-dir=<Your chrome profile>")
driver = uc.Chrome(options=options, executable_path="/usr/bin/chromedriver")
url='https://accounts.google.com/servicelogin'
driver.get(url)