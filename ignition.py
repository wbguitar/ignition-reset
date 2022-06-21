import traceback, sys, time

import msedge.selenium_tools
import selenium.webdriver.common.by
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def run(config):
    driver = None
    timeout = 5.0
    try:
        if config['webdriver'].lower() == 'edge':
            opt = msedge.selenium_tools.EdgeOptions()
            if config.get('headless', False):
                opt.use_chromium = True
                opt.add_argument('--headless')
            driver = msedge.selenium_tools.webdriver.WebDriver('msedgedriver.exe', options=opt)
        elif config['webdriver'].lower() == 'firefox':
            driver = webdriver.Firefox() # TO BE TESTED
        elif config['webdriver'].lower() == 'chrome':
            opt = Options()
            if config.get('headless', False):
                opt.add_argument('--headless')
            try:
                driver = webdriver.Chrome(options=opt)
            except selenium.common.SessionNotCreatedException:
                # driver not compatible?
                drv_path = ChromeDriverManager().install()
                driver = webdriver.Chrome(drv_path, options=opt)

        # driver.minimize_window()
        driver.get(config['gateway'])

        def element_loaded(*selector):
            try:
                return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(selector))
            except selenium.common.TimeoutException:
                raise selenium.common.TimeoutException(msg=f"Timeout while loading {[it for it in selector]}")

        # expired = driver.find_element(By.CSS_SELECTOR, 'div.alert-left h2').text
        expired = element_loaded(By.CSS_SELECTOR, 'div.alert-left h2').text
        if expired != 'Trial Expired':
            return

        # go to login page
        # driver.find_element(By.ID, 'login-link').click()
        element_loaded(By.ID, 'login-link').click()
        # set auth fields and login
        # driver.find_element(By.CSS_SELECTOR, 'input.username-field').send_keys(config['auth']['username'])
        element_loaded(By.CSS_SELECTOR, 'input.username-field').send_keys(config['auth']['username'])
        # driver.find_element(By.CSS_SELECTOR, 'div.submit-button').click()
        element_loaded(By.CSS_SELECTOR, 'div.submit-button').click()
        # driver.find_element(By.CSS_SELECTOR, 'input.password-field').send_keys(config['auth']['password'])
        element_loaded(By.CSS_SELECTOR, 'input.password-field').send_keys(config['auth']['password'])
        # driver.find_element(By.CSS_SELECTOR, 'div.submit-button').click()
        element_loaded(By.CSS_SELECTOR, 'div.submit-button').click()
        # reset trial
        element_loaded(By.CSS_SELECTOR, 'a#reset-trial-anchor').click()
    except TimeoutException:
        print(f"Timeout: {traceback.format_exc()}")
    except SessionNotCreatedException:
        print(f"Cannot create session: {traceback.format_exc()}")
    except Exception as e:
        print(traceback.format_exc())
    finally:
        if driver:
            if not config.get('headless', False):
                time.sleep(3) #
            driver.quit()


