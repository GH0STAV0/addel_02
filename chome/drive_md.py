from selenium import webdriver
from selenium_stealth import stealth
import time
import cnf

def build_driver():

        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        # options.add_argument( "--user-data-dir=profile")
        options.add_argument('--disable-blink-features=AutomationControlled')
        # options.add_argument("--lang=fr")
        # options.add_argument(cnf.user_agent)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options, executable_path="/usr/bin/chromedriver")

        stealth(driver,
                user_agent=cnf.user_agent,
                # languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                )
        return driver
        # url = "https://bot.sannysoft.com/"
        # driver.get(url)

        # input("")
        # url='https://accounts.google.com/servicelogin'

        # driver.get(url)
        # time.sleep(5)
        # input("")
        # driver.quit()