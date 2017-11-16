# -*- coding: utf-8 -*-
import time
import unittest
import uuid

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class TestRegisterInstituicaoDefault(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_register_instituicao_default(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(1)
        driver.find_element_by_id("inscrevase_link").click()
        driver.find_element_by_id("register_instituicao_link").click()
        time.sleep(1)
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Instituicao 1")
        driver.find_element_by_id("id_cnpj").clear()
        driver.find_element_by_id("id_cnpj").send_keys("27.974.463/0001-00")
        driver.find_element_by_id("id_cep").clear()
        driver.find_element_by_id("id_cep").send_keys("12345654")
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
        driver.find_element_by_id("id_phone").clear()
        driver.find_element_by_id("id_phone").send_keys("(83) 9887 31795")
        driver.find_element_by_id("id_complement").clear()
        driver.find_element_by_id("id_complement").send_keys("Nenhum")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("teste@gmail.com")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("instituicao-" + str(uuid.uuid4()))
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("abcde")
        time.sleep(1)
        driver.find_element_by_id("btn_salvar").click()
        try:
            self.assertEqual(u"Nova Instituição cadastrada com sucesso.",
                             driver.find_element_by_xpath("//div[3]/p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        time.sleep(1)
        driver.find_element_by_css_selector("button.confirm").click()

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
