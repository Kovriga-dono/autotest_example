import pages.main_page
import pages.base_page
from conftest import browser
import allure
import os



# тесты для Chrome и FireFox будут запускаться для Winows, MacOS и Linux
# запускает тест для браузера Chome
@allure.feature('autotest example')
@allure.story('filling Chrome')
def test_fill_contact(browser):
    # открываем браузер
    with allure.step('open browser Chrome'):
        main_page = pages.main_page.MainPage(browser)
        # переходим на тестируемую страницу
    main_page.open()
    # заполняем данные контакта; создаем контакт; проверяем счетчик
    main_pageс = pages.main_page.MainPage(browser)
    main_pageс.fill_contact_name()
    main_pageс.fill_contact_lastname()
    main_pageс.fill_contact_category()
    main_pageс.fill_contact_bday()
    main_pageс.fill_contact_addres()
    with allure.step('close browser'):
        browser.quit()


@allure.feature('autotest example')
@allure.story('filling Chrome')
def test_fill_contact_f(browser_f):
    # открываем браузер
    with allure.step('open browser FireFox'):
        main_page = pages.main_page.MainPage(browser_f)
        # переходим на тестируемую страницу
    main_page.open()
    # заполняем данные контакта; создаем контакт; проверяем счетчик
    main_pagef = pages.main_page.MainPage(browser_f)
    main_pagef.fill_contact_name()
    main_pagef.fill_contact_lastname()
    main_pagef.fill_contact_category()
    main_pagef.fill_contact_bday()
    main_pagef.fill_contact_addres()
    with allure.step('close browser'):
        browser_f.quit()


if os.name == 'nt':
    @allure.feature('autotest example')
    @allure.story('filling EDGE')
    def test_fill_contact_e(browser_e):
        # открываем браузер
        with allure.step('open browser Chrome'):
            main_page = pages.main_page.MainPage(browser_e)
            # переходим на тестируемую страницу
        main_page.open()
        # заполняем данные контакта; создаем контакт; проверяем счетчик
        main_pagee = pages.main_page.MainPage(browser_e)
        main_pagee.fill_contact_name()
        main_pagee.fill_contact_lastname()
        main_pagee.fill_contact_category()
        main_pagee.fill_contact_bday()
        main_pagee.fill_contact_addres()
        with allure.step('close browser'):
            browser_e.quit()

if os.name == 'mac':
    @allure.feature('autotest example')
    @allure.story('filling Safari')
    def test_fill_contact_s(browser_s):
        # открываем браузер
        with allure.step('open browser Chrome'):
            main_page = pages.main_page.MainPage(browser_s)
            # переходим на тестируемую страницу
        main_page.open()
        # заполняем данные контакта; создаем контакт; проверяем счетчик
        main_pages = pages.main_page.MainPage(browser_s)
        main_pages.fill_contact_name()
        main_pages.fill_contact_lastname()
        main_pages.fill_contact_category()
        main_pages.fill_contact_bday()
        main_pages.fill_contact_addres()
        with allure.step('close browser'):
            browser_s.quit()
