# -*- coding: utf-8 -*-
import time
import unittest
import uuid

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException


class TestRegisterUserDefault(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_register_user_default(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        time.sleep(5)
        driver.find_element_by_id("inscrevase_link").click()
        driver.find_element_by_id("register_user_link").click()
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("Teste")
        driver.find_element_by_id("id_last_name").clear()
        driver.find_element_by_id("id_last_name").send_keys("Testee")
        driver.find_element_by_id("cpf").clear()
        driver.find_element_by_id("cpf").send_keys("1112223345")
        driver.find_element_by_id("id_birth_date").clear()
        driver.find_element_by_id("id_birth_date").send_keys("1995-01-19")
        driver.find_element_by_id("cep").clear()
        driver.find_element_by_id("cep").send_keys("12345654")
        driver.find_element_by_id("estado").clear()
        driver.find_element_by_id("estado").send_keys("Paraiba")
        driver.find_element_by_id("cidade").clear()
        driver.find_element_by_id("cidade").send_keys("Campina Grande")
        driver.find_element_by_id("bairro").clear()
        driver.find_element_by_id("bairro").send_keys("Prata")
        driver.find_element_by_id("rua").clear()
        driver.find_element_by_id("rua").send_keys("Rua Montevideo")
        driver.find_element_by_id("numero").clear()
        driver.find_element_by_id("numero").send_keys("78")
        driver.find_element_by_id("complemento").clear()
        driver.find_element_by_id("complemento").send_keys("Perto da Padaria")
        driver.find_element_by_id("telefone").clear()
        driver.find_element_by_id("telefone").send_keys("988776655")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("teste@gmail.com")
        driver.find_element_by_id("id_username").clear()
        time.sleep(1)
        driver.find_element_by_id("id_username").send_keys("teste-" + str(uuid.uuid4()))
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("teste")
        time.sleep(1)
        driver.find_element_by_id("subscribe").clear()
        driver.find_element_by_id("subscribe").send_keys("test")
        driver.find_element_by_class_name("btn-success").is_displayed()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='btn_salvar']").click()
        time.sleep(1)
        try:
            self.assertEqual(u"Novo usuário cadastrado com sucesso.", driver.find_element_by_xpath("//div[3]/p").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("Sucesso", driver.find_element_by_xpath("//div[3]/h2").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
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
