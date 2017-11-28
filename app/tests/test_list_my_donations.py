# -*- coding: utf-8 -*-
import unittest
import uuid

import time
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class TestListMyDonations(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_list_my_donations(self):
        driver = self.driver
        username = "teste-" + str(uuid.uuid4())
        driver.get(self.base_url + "/")
        driver.find_element_by_id("inscrevase_link").click()
        driver.find_element_by_id("register_user_link").click()
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Teste " + str(uuid.uuid4()))
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Fulano")
        driver.find_element_by_id("id_cpf").clear()
        driver.find_element_by_id("id_cpf").send_keys("111.111.111-11")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("teste@gmail.com")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(username)
        driver.find_element_by_id("id_birth_date").clear()
        driver.find_element_by_id("id_birth_date").send_keys("1995-12-12")
        driver.find_element_by_id("id_phone").clear()
        driver.find_element_by_id("id_phone").send_keys("(11)11111-1111")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("teste")
        driver.find_element_by_id("subscribe").clear()
        driver.find_element_by_id("subscribe").send_keys("abcde")
        driver.find_element_by_id("btn_salvar").click()
        driver.find_element_by_css_selector("button.confirm").click()
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(username)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("teste")
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_css_selector("span.hidden-xs.text-uppercase").click()
        driver.find_element_by_css_selector("#my_objects > a > span").click()
        try:
            self.assertEqual(u"Minhas Doações", driver.find_element_by_css_selector("div.box-header > p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        time.sleep(2)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
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
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
