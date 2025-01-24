import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from wait_for_download import wait_for_download


def get_covered_entity_daily(download_dir, snapshot_date):
    options = Options()

    browser = webdriver.Firefox(options=options)
    options.set_preference("browser.download.folderList", 2)
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", download_dir)
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/json")

    try:
        browser.get("https://340bopais.hrsa.gov/reports")
        wait = WebDriverWait(browser, 10)
        button = wait.until(
            EC.element_to_be_clickable((By.ID, "ctl00_ContentPlaceHolder1_lnkCEDailyJSONDump"))
        )

        browser.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
        button.click()
        brower.quit()

        while not wait_for_download(download_dir):
            time.sleep(1)
    finally:
            browser.quit()




