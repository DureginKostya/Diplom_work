from pages.hamburger_menu_page import HamburgerMenuPage
from pages.locators import HamburgerMenuPageLocators, HeaderPageLocators, BackCallPageLocators
import yaml

with open("data/testdata_header_hamburger_menu.yaml", encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw42(browser):
    contents = (HeaderPageLocators.LOCATOR_BUTTON_RANSOM, HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                HeaderPageLocators.LOCATOR_BUTTON_REVIEWS, HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU_CLOSE)
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.changed_window_size(1280, 728)
    test_page.checking_contents_page(contents, HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU)


def test_dw43(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button_navigation(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                      HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                      'ransom')


def test_dw44(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                   data['title_btn_ransom'])


def test_dw45(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                   'font-family',
                                   data['font'])


def test_dw46(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                        HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                        'font-size',
                                        data['font_size_title_ransom'])


def test_dw47(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                         HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                         'color',
                                         data['font_color_title_ransom'])


def test_dw48(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button_navigation(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                      HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                      'questions_answers')


def test_dw49(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   data['title_btn_questions_answers'])


def test_dw50(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   'font-family',
                                   data['font'])


def test_dw51(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                        HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                        'font-size',
                                        data['font_size_title_questions_answers'])


def test_dw52(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                         HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                         'color',
                                         data['font_color_title_questions_answers'])


def test_dw53(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button_navigation(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                      HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                      'reviews')


def test_dw54(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   data['title_btn_reviews'])


def test_dw55(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   'font-family',
                                   data['font'])


def test_dw56(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                        HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                        'font-size',
                                        data['font_size_title_reviews'])


def test_dw57(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                         HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                         'color',
                                         data['font_color_title_reviews'])


def test_dw58(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                           HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                           BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS,
                           data['title_leave_contacts'])


def test_dw59(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   data['title_btn_call_back'])


def test_dw60(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'font-family',
                                   data['font'])


def test_dw61(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                        HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                        'font-size',
                                        data['font_size_title_call_back'])


def test_dw62(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                         HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                         'color',
                                         data['font_color_title_call_back_not_cursor'])


def test_dw63(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                               HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                               'background-color',
                                               data['background_color_btn_call_back_not_cursor'])


def test_dw64(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                               HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                               'background-image',
                                               data['background_color_btn_call_back_with_cursor'],
                                               1)


def test_dw65(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                         HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                         'color',
                                         data['font_color_title_call_back_with_cursor'],
                                         1)


def test_dw67(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_size_button(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'height',
                                   'width',
                                   data['height_btn_call_back'],
                                   data['width_call_back'])


def test_dw68(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_RANSOM,
                                   'cursor',
                                   data['type_cursor_btn_ransom'])


def test_dw69(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   'cursor',
                                   data['type_cursor_btn_questions_answers'])


def test_dw70(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HeaderPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   'cursor',
                                   data['type_cursor_btn_reviews'])


def test_dw71(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HamburgerMenuPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'cursor',
                                   data['type_cursor_btn_call_back'])


def test_dw72(browser):
    test_page = HamburgerMenuPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU,
                                   HamburgerMenuPageLocators.LOCATOR_BUTTON_HAMBURGER_MENU_CLOSE,
                                   'cursor',
                                   data['type_cursor_close_hamburger_menu'])
    test_page.driver.maximize_window()
