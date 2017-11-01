# -*- coding: utf-8 -*-
"""test_login_admin_verify_list_login.py: Testes de Login valido na pagina de admin do Django ."""

__author__ = "Caio Marinho"
__copyright__ = "Copyright 2017, LES-UFCG"

import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class TestLoginAdminVerifyListLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_admin_verify_list_login(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/login/?next=/admin/")
        try:
            self.assertEqual(u"Usuário:", driver.find_element_by_css_selector("label.required").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("Senha:", driver.find_element_by_xpath("//form[@id='login-form']/div[2]/label").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "input[type=\"submit\"]"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("admin")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("12345678")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        try:
            self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "#content > h1"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual(u"Administração do Site", driver.find_element_by_css_selector("#content > h1").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"Usuários").click()
        try:
            self.assertTrue(self.is_element_present(By.LINK_TEXT, "admin"))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        try:
            self.assertEqual("admin", driver.find_element_by_link_text("admin").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

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
