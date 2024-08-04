from pages.base_page import BasePage
import re
import models.lib
import allure

# открываем браузер
class MainPage(BasePage):

    def open(self):
        with allure.step('open page'):
            self.browser.get(models.lib.test_func)

    # наполняем данными
    def fill_contact_page(self):
        with allure.step('filling data'):
            # берем оригинальное значение счетчика
            c = re.search(r'\d+$', self.find(models.lib.counter_selector).text).group()
            # заполняем контактные данные
            self.find(models.lib.firstname_selector).send_keys(models.lib.contact.first_name)
            self.find(models.lib.lastname_selector).send_keys(models.lib.contact.last_name)
            self.find(models.lib.category_selector).send_keys(models.lib.contact.category)
            self.find(models.lib.birthday_selector).send_keys(models.lib.contact.birthday)
            self.find(models.lib.firstname_selector).click()
            self.find(models.lib.addres_selector).send_keys(models.lib.contact.address)
            self.find(models.lib.button_selector).click()
            # берём счетчик после создания контакта
            b = re.search(r'\d+$', self.find(models.lib.counter_selector).text).group()
            # сравниваем счетчик до и после создания контакта
            assert int(b) == int(c) + 1
