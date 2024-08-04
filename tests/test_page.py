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
    with allure.step('open Chrome'):
    # открываем браузер
        main_page = pages.main_page.MainPage(browser)
        # переходим на тестируемую страницу
    main_page.open()
    # заполняем данные контакта; создаем контакт; проверяем счетчик
    main_pageс = pages.main_page.MainPage(browser)
    main_pageс.fill_contact_page()
    with allure.step('browser closed'):
        browser.quit()

# запускает тест для браузера FireFox
@allure.feature('autotest example')
@allure.story('filling FireFox')
def test_fill_contact_f(browser_f):
    with allure.step('open browser FireFox'):
        main_page = pages.main_page.MainPage(browser_f)
    main_page.open()
    main_pagef = pages.main_page.MainPage(browser_f)
    main_pagef.fill_contact_page()
    with allure.step('close browser'):
        browser_f.quit()

#EDGE тестируем только для Windows
if os.name == 'nt':
    # запускает тест для браузера EDGE
    @allure.feature('autotest example')
    @allure.story('filling Edge')
    def test_fill_contact_e(browser_e):
        with allure.step('open browser Edge'):
            main_page = pages.main_page.MainPage(browser_e)
        main_page.open()
        main_pagee = pages.main_page.MainPage(browser_e)
        main_pagee.fill_contact_page()
        with allure.step('close browser'):
            browser_e.quit()

#Safari тестируем только в MacOS
elif os.name == 'mac':
    # запускает тест для браузера EDGE
    @allure.feature('autotest example')
    @allure.story('filling Safari')
    def test_fill_contact_m(browser_m):
        with allure.step('open Safari'):
            main_page = pages.main_page.MainPage(browser_m)
        main_page.open()
        main_pagem = pages.main_page.MainPage(browser_m)
        main_pagem.fill_contact_page()
        with allure.step('close browser'):
            browser_m.quit()
