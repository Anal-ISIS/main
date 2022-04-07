import selenium
import undetected_chromedriver
import time
from selenium.webdriver.common.by import By

from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

GECKODRIVER_PATH = ('/home/nick/ANAL_ISIS/requests/geckodriver')

basic_folder = ("/home/nick/ANAL_ISIS/anal_isis/download_manager/download_files")


def driver_call(download_folder=basic_folder,display_gui = True):
    ser = Service(GECKODRIVER_PATH)
    option = webdriver.FirefoxOptions()
    option.set_preference("browser.download.folderList", 2)
    option.set_preference("browser.download.manager.showWhenStarting", False)

    option.set_preference("browser.download.dir", download_folder)
    option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

    option.headless = display_gui  # True == do not display browser GUI

    driver = webdriver.Firefox(service=ser, options=option)

    driver.set_page_load_timeout(5)
    return driver

# try:
#     driver_call().get('https://www.sec.gov/Archives/edgar/data/0000050863/000005086321000038/Financial_Report.xlsx')
# except :
#     driver_call().quit()

# try:
#     driver = driver_call()
#     driver.get('https://www.sec.gov/files/company_tickers.json')
#     page_1 = driver.find_element(By.TAG_NAME, "body")
#     driver.quit()
#     # print(page_1.text)
# except :
#     pass
# finally:
#     pass