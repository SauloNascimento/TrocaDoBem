# -*- coding: utf-8 -*-
import time
import unittest
import uuid

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class TestLoginUserDefault(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_user_default(self):
        username = "teste-" + str(uuid.uuid4())
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(1)
        driver.find_element_by_id("inscrevase_link").click()
        time.sleep(3)
        time.sleep(1)
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Caio")
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Marinho")
        driver.find_element_by_id("id_cpf").clear()
        driver.find_element_by_id("id_cpf").send_keys("125.381.179-25")
        driver.find_element_by_id("id_birth_date").clear()
        driver.find_element_by_id("id_birth_date").send_keys("1995-01-19")
        driver.find_element_by_id("id_cep").clear()
        driver.find_element_by_id("id_cep").send_keys("58423-530")
        driver.find_element_by_id("id_state").clear()
        driver.find_element_by_id("id_state").send_keys("PB")
        driver.find_element_by_id("id_city").clear()
        driver.find_element_by_id("id_city").send_keys("Campina grande")
        driver.find_element_by_id("id_district").clear()
        driver.find_element_by_id("id_district").send_keys("Tres Irmas")
        driver.find_element_by_id("id_address").clear()
        driver.find_element_by_id("id_address").send_keys(u"Rua Cláudio Bezerra de Lima")
        driver.find_element_by_id("id_number").clear()
        driver.find_element_by_id("id_number").send_keys("694")
        driver.find_element_by_id("id_complement").clear()
        driver.find_element_by_id("id_complement").send_keys("Nenhum")
        driver.find_element_by_id("id_phone").clear()
        driver.find_element_by_id("id_phone").send_keys("(83) 9887 31795")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("teste@gmail.com")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(username)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("abcde")
        driver.find_element_by_id("subscribe").clear()
        driver.find_element_by_id("subscribe").send_keys("teste")
        driver.find_element_by_id("btn_salvar").click()
        time.sleep(1)
        driver.find_element_by_css_selector("button.confirm").click()
        driver.find_element_by_css_selector("span.hidden-xs.text-uppercase").click()
        time.sleep(1)
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys(username)
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("abcde")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)
        driver.find_element_by_css_selector("span.hidden-xs.text-uppercase").click()
        time.sleep(1)

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
