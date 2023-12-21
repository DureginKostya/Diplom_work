from pages.header_page import HeaderPage
from pages.locators import (HeaderPageLocators, BackCallPageLocators, HamburgerMenuPageLocators)
import yaml
import pytest

with open("data/testdata_header_hamburger_menu.yaml", encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw1(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_title(data['title_landing'])


def test_dw2(browser):
    contents = (HeaderPageLocators.LOCATOR_BUTTON_RANSOM, HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                HeaderPageLocators.LOCATOR_BUTTON_REVIEWS, HeaderPageLocators.LOCATOR_BUTTON_CALL,
                HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_contents_page(contents)


def test_dw3(browser):
    contents = (HeaderPageLocators.LOCATOR_BUTTON_RANSOM, HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                HeaderPageLocators.LOCATOR_BUTTON_REVIEWS, HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.changed_window_size(1280, 728)
    test_page.checking_not_contents_page(contents, HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU)
    test_page.driver.maximize_window()


def test_dw4(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button_navigation(HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                      'ransom')


def test_dw5(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                   data['title_btn_ransom'])


def test_dw6(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                   'font-family',
                                   data['font'])


def test_dw7(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                        'font-size',
                                        data['font_size_title_ransom'])


def test_dw8(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                         'color',
                                         data['font_color_title_ransom'])


def test_dw9(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button_navigation(HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                      'questions_answers')


def test_dw10(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   data['title_btn_questions_answers'])


def test_dw11(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   'font-family',
                                   data['font'])


def test_dw12(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                        'font-size',
                                        data['font_size_title_questions_answers'])


def test_dw13(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                         'color',
                                         data['font_color_title_questions_answers'])


def test_dw14(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button_navigation(HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                      'reviews')


def test_dw15(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   data['title_btn_reviews'])


def test_dw16(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   'font-family',
                                   data['font'])


def test_dw17(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                        'font-size',
                                        data['font_size_title_reviews'])


def test_dw18(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                         'color',
                                         data['font_color_title_reviews'])


@pytest.mark.skip(reason="no way of currently testing this")
def test_dw19(browser):
    pass


def test_dw20(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HeaderPageLocators.LOCATOR_BUTTON_CALL,
                                   data['title_btn_call'])


def test_dw21(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HeaderPageLocators.LOCATOR_BUTTON_CALL,
                                   'font-family',
                                   data['font'])


def test_dw22(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HeaderPageLocators.LOCATOR_BUTTON_CALL,
                                        'font-size',
                                        data['font_size_title_call'])


def test_dw23(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HeaderPageLocators.LOCATOR_BUTTON_CALL,
                                         'color',
                                         data['font_color_title_call'])


def test_dw24(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                           BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS,
                           data['title_leave_contacts'])


def test_dw25(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   data['title_btn_call_back'])


def test_dw26(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'font-family',
                                   data['font'])


def test_dw27(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                        'font-size',
                                        data['font_size_title_call_back'])


def test_dw28(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                         'color',
                                         data['font_color_title_call_back_not_cursor'])


def test_dw29(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                               'background-color',
                                               data['background_color_btn_call_back_not_cursor'])


def test_dw30(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                               'background-image',
                                               data['background_color_btn_call_back_with_cursor'],
                                               1)


def test_dw31(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                         'color',
                                         data['font_color_title_call_back_with_cursor'],
                                         1)


def test_dw33(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_size_button(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'height',
                                   'width',
                                   data['height_btn_call_back'],
                                   data['width_call_back'])


def test_dw34(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.changed_window_size(1280, 728)
    test_page.click_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                           HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                           data['title_btn_ransom'])
    test_page.driver.maximize_window()


def test_dw35(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.changed_window_size(1280, 728)
    test_page.checking_close_hamburger_menu(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                            HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU_CLOSE,
                                            HeaderPageLocators.LOCATOR_BUTTON_RANSOM)
    test_page.driver.maximize_window()


def test_dw36(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                   'cursor',
                                   data['type_cursor_btn_ransom'])


def test_dw37(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   'cursor',
                                   data['type_cursor_btn_questions_answers'])


def test_dw38(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   'cursor',
                                   data['type_cursor_btn_reviews'])


def test_dw39(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HeaderPageLocators.LOCATOR_BUTTON_CALL,
                                   'cursor',
                                   data['type_cursor_btn_call'])


def test_dw40(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'cursor',
                                   data['type_cursor_btn_call_back'])


def test_dw41(browser):
    test_page = HeaderPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_favicon(HeaderPageLocators.LOCATOR_FAVICON, 'favicon')
