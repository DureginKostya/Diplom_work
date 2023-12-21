import time
from pages.thank_you_winsow_page import ThankYouWindowPage
from pages.locators import ThankYouWindowPageLocators, MainPageLocators
import yaml


with open('data/testdata_thank_you_window.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw821(browser):
    contents = (ThankYouWindowPageLocators.LOCATOR_TITLE, ThankYouWindowPageLocators.LOCATOR_SUBTITLE,
                ThankYouWindowPageLocators.LOCATOR_ICON)
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw822(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_name_text(ThankYouWindowPageLocators.LOCATOR_TITLE,
                                 data['title_thank_you_window'])


def test_dw823(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_font_text(ThankYouWindowPageLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw824(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_font_size_text(ThankYouWindowPageLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_thank_you_window'])


def test_dw825(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_font_color_text(ThankYouWindowPageLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_title_thank_you_window'])


def test_dw826(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_name_text(ThankYouWindowPageLocators.LOCATOR_SUBTITLE,
                                 data['subtitle_thank_you_window'])


def test_dw827(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_font_text(ThankYouWindowPageLocators.LOCATOR_SUBTITLE,
                                 'font-family',
                                 data['font'])


def test_dw828(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_font_size_text(ThankYouWindowPageLocators.LOCATOR_SUBTITLE,
                                      'font-size',
                                      data['font_size_subtitle_thank_you_window'])


def test_dw829(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_font_color_text(ThankYouWindowPageLocators.LOCATOR_SUBTITLE,
                                       'color',
                                       data['font_color_subtitle_thank_you_window'])


def test_dw830(browser):
    test_page = ThankYouWindowPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_thank_you(MainPageLocators.LOCATOR_BUTTON_SELL, MainPageLocators.LOCATOR_FIELD_PHONE,
                                    '+79999999999')
    time.sleep(2)
    test_page.checking_icon(ThankYouWindowPageLocators.LOCATOR_ICON,
                            data['title_icon'])
