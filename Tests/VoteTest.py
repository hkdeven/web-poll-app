# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class VoteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:5000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_vote(self):
        driver = self.driver
        driver.get(self.base_url + "/polls")
        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_xpath("//input[@type='email']").clear()
        driver.find_element_by_xpath("//input[@type='email']").send_keys("feghhi@ualberta.ca")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("secret")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_link_text("question test").click()
        driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/div/div/span/input").click()
        driver.find_element_by_link_text("Ask Everybody").click()
        driver.find_element_by_link_text("question test").click()
        self.assertTrue(driver.find_element_by_xpath("/html/body/div/div[2]/div/div[1]/div/div/div/span/input").is_selected())
        driver.find_element_by_link_text("Log out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
