import selenium.webdriver.common.by
from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def run(config):
    driver = None
    try:
        if config['webdriver'].lower() == 'edge':
            driver = webdriver.Edge()
        elif config['webdriver'].lower() == 'firefox':
            driver = webdriver.Firefox()
        elif config['webdriver'].lower() == 'chrome':
            driver = webdriver.Chrome()

        # driver.minimize_window()
        driver.get(config['gateway'])

        cdown = driver.find_element(By.CSS_SELECTOR, 'p.countdown').text
        # if trial is not reset exits
        if cdown != "0:00:00":
            return

        # go to login page
        driver.find_element(By.ID, 'login-link').click()
        # set auth fields and login
        driver.find_element(By.CSS_SELECTOR, 'input.username-field').send_keys(config['auth']['username'])
        driver.find_element(By.CSS_SELECTOR, 'div.submit-button').click()
        driver.find_element(By.CSS_SELECTOR, 'input.password-field').send_keys(config['auth']['password'])
        driver.find_element(By.CSS_SELECTOR, 'div.submit-button').click()
        # reset trial
        driver.find_element(By.CSS_SELECTOR, 'a#reset-trial-anchor').click()
        time.sleep(2.0)
    finally:
        if driver:
            driver.quit()
