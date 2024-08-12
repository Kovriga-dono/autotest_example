from pages.base_page import BasePage
import re
import models.lib
import allure


# открываем браузер
class MainPage(BasePage):

    def open(self):
        self.browser.get(models.lib.test_func)

    def fill_contact_name(self):
        with allure.step('filling name'):
            self.find(models.lib.firstname_selector).send_keys(models.lib.contact.first_name)

    def fill_contact_lastname(self):
        with allure.step('filling lastname'):
            self.find(models.lib.lastname_selector).send_keys(models.lib.contact.last_name)

    def fill_contact_category(self):
        with allure.step('filling category'):
            self.find(models.lib.category_selector).send_keys(models.lib.contact.category)

    def fill_contact_bday(self):
        with allure.step('filling birthday'):
            self.find(models.lib.birthday_selector).send_keys(models.lib.contact.birthday)
            self.find(models.lib.firstname_selector).click()

    def fill_contact_addres(self):
        with allure.step('filling addres'):
            c = re.search(r'\d+$', self.find(models.lib.counter_selector).text).group()
            self.find(models.lib.addres_selector).send_keys(models.lib.contact.address)
            self.find(models.lib.button_selector).click()
            # берём счетчик после создания контакта
            b = re.search(r'\d+$', self.find(models.lib.counter_selector).text).group()
            # сравниваем счетчик до и после создания контакта
            assert int(b) == int(c) + 1
