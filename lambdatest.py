from selenium import webdriver
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
def test_lambdatest_todo_app():
   ff_driver = webdriver.Edge()
   ff_driver.get('https://lambdatest.github.io/sample-todo-app/')
   ff_driver.maximize_window()
   ff_driver.find_element_by_name("li1").click()
   ff_driver.find_element_by_name("li2").click()
   title = "Sample page - lambdatest.com"
   assert title == ff_driver.title
   sample_text = "Happy Testing at LambdaTest"
   email_text_field = ff_driver.find_element_by_id("sampletodotext")
   email_text_field.send_keys(sample_text)
   sleep(5)
   ff_driver.find_element_by_id("addbutton").click()
   sleep(5)
   output_str = ff_driver.find_element_by_name("li6").text
   sys.stderr.write(output_str)
   sleep(2)
   ff_driver.quit()