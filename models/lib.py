import random
import string
from selenium.webdriver.common.by import By
from models.contact import Fields


# счетчик контактов
counter_selector = (By.XPATH, '//div[@dir="ltr"]')

# кнопка создания контакта
button_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[7]/td/button[2]')

firstname_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[2]/td[2]/input')
lastname_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[3]/td[2]/input')
category_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[4]/td[2]/select')
birthday_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[5]/td[2]/input')
addres_selector = (By.XPATH, '//div[@class="middleCenterInner"]/div/table/tbody/tr[6]/td[2]/textarea')

catt = ('Friends', 'Coworkers', 'Family', 'Business', 'Contacts')

test_func = ('https://samples.gwtproject.org/samples/Showcase/Showcase.html#!CwCellList')


class Filling:

    def letters(x):
        let = (random.choice(string.ascii_lowercase) for x in range(5))
        return let

    def numbers(x):
        num = (random.choice(string.digits) for x in range(x))
        return num

    def categ():
        cho = (random.choice(catt))
        return cho


contact = Fields(Filling.letters(5),
                 Filling.letters(10),
                 Filling.categ(),
                 Filling.numbers(8),
                 "June 11, 2001")

