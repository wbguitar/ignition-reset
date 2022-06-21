import traceback

import selenium.webdriver.common.by
from selenium import webdriver
import sys

from selenium.common import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def run(config):
    driver = None
    wait = 0.5
    timeout = 5.0

    try:
        if config['webdriver'].lower() == 'edge':
            driver = webdriver.Edge()
        elif config['webdriver'].lower() == 'firefox':
            driver = webdriver.Firefox()
        elif config['webdriver'].lower() == 'chrome':
            driver = webdriver.Chrome()

        # driver.minimize_window()
        driver.get(config['gateway'])

        def element_loaded(*selector):
            try:
                return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(selector))
            except TimeoutException:
                raise TimeoutException(msg=f"Timeout while loading {[it for it in selector]}")

        # expired = driver.find_element(By.CSS_SELECTOR, 'div.alert-left h2').text
        expired = element_loaded(By.CSS_SELECTOR, 'div.alert-left h2').text
        # if expired != 'Trial Expired':
        #     return

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
    except Exception as e:
        print(traceback.format_exc())
    finally:
        if driver:
            driver.quit()
