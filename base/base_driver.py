import time

import selenium.webdriver.common.driver_finder
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self,driver):
        self.driver = driver

    def dynamic_scrolling(self):
        while True:
            old_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == old_height:
                break

    def wait_for_presence_of_element_located(self,locator_type,locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((locator_type,locator)))


    def wait_for_text_to_be_present_in_element_attribute(self,locator_type,locator,attribute,text):
        wait = WebDriverWait(self.driver, 50)
        wait.until(
            EC.text_to_be_present_in_element_attribute((locator_type, locator), attribute, text))

    def wait_until_element_not_present(self,locator_type,locator):
        wait =  WebDriverWait(self.driver,10)
        wait.until_not(EC.presence_of_element_located((locator_type,locator)))

    def wait_for_frame_to_be_available_and_switch(self,locator_type,locator):
        wait =  WebDriverWait(self.driver,10)
        wait.until(EC.frame_to_be_available_and_switch_to_it((locator_type,locator)))

    def scroll_to_element_custom(self,element):
        action = ActionChains(self.driver)
        action.scroll_to_element(element).perform()

    def wait_for_element_to_be_clickable(self,locator_type,locator):
        wait = WebDriverWait(self.driver,10)
        wait.until(EC.element_to_be_clickable((locator_type,locator)))

    def test_method(self):
        pass

    def test_method_sdet_2(self):
        pass




