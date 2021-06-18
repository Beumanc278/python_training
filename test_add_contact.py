# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

from selenium.webdriver.support.select import Select

from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username='admin', password='secret')
        self.open_create_contact_page(wd)
        self.create_contact(wd, Contact(first_name='testFirstname',
                                        last_name='testLastname',
                                        address='testAddress',
                                        phone='9994443322',
                                        email='testemail@testdomain.com'))
        self.return_to_home_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_create_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def create_contact(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name('lastname').send_keys(contact.last_name)
        wd.find_element_by_name('address').send_keys(contact.address)
        wd.find_element_by_name('mobile').send_keys(contact.phone)
        wd.find_element_by_name('email').send_keys(contact.email)
        # select default group
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()