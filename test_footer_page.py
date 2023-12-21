import time
from pages.footer_page import FooterPage
from pages.locators import FooterPageLocators, BackCallPageLocators
import yaml
import pytest

with open("data/testdata_footer.yaml", encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw714(browser):
    contents = (FooterPageLocators.LOCATOR_BUTTON_RANSOM, FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                FooterPageLocators.LOCATOR_BUTTON_REVIEWS, FooterPageLocators.LOCATOR_BUTTON_CALL,
                FooterPageLocators.LOCATOR_BUTTON_CALL_BACK, FooterPageLocators.LOCATOR_REGISTERED_SYMBOL,
                FooterPageLocators.LOCATOR_CREATE_LANDING, FooterPageLocators.LOCATOR_POLICY)
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw715(browser):
    contents = (FooterPageLocators.LOCATOR_BUTTON_RANSOM, FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                FooterPageLocators.LOCATOR_BUTTON_REVIEWS)
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.changed_window_size(1280, 728)
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_not_contents_page(contents)
    test_page.driver.maximize_window()


def test_dw716(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.click_button_navigation(FooterPageLocators.LOCATOR_BUTTON_RANSOM,
                                      'ransom')


def test_dw717(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_BUTTON_RANSOM,
                                   data['title_btn_ransom'])


def test_dw718(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_BUTTON_RANSOM,
                                   'font-family',
                                   data['font'])


def test_dw719(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_BUTTON_RANSOM,
                                        'font-size',
                                        data['font_size_title_ransom'])


def test_dw720(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_BUTTON_RANSOM,
                                         'color',
                                         data['font_color_title_ransom'])


def test_dw721(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.click_button_navigation(FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                      'questions_answers')


def test_dw722(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   data['title_btn_questions_answers'])


def test_dw723(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   'font-family',
                                   data['font'])


def test_dw724(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                        'font-size',
                                        data['font_size_title_questions_answers'])


def test_dw725(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                         'color',
                                         data['font_color_title_questions_answers'])


def test_dw726(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.click_button_navigation(FooterPageLocators.LOCATOR_BUTTON_REVIEWS,
                                      'reviews')


def test_dw727(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   data['title_btn_reviews'])


def test_dw728(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   'font-family',
                                   data['font'])


def test_dw729(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_BUTTON_REVIEWS,
                                        'font-size',
                                        data['font_size_title_reviews'])


def test_dw730(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_BUTTON_REVIEWS,
                                         'color',
                                         data['font_color_title_reviews'])


@pytest.mark.skip(reason="no way of currently testing this")
def test_dw731(browser):
    pass


def test_dw732(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_BUTTON_CALL,
                                   data['title_btn_call'])


def test_dw733(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_BUTTON_CALL,
                                   'font-family',
                                   data['font'])


def test_dw734(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_BUTTON_CALL,
                                        'font-size',
                                        data['font_size_title_call'])


def test_dw735(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_BUTTON_CALL,
                                         'color',
                                         data['font_color_title_call'])


def test_dw737(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   data['title_btn_call_back'])


def test_dw738(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'font-family',
                                   data['font'])


def test_dw739(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                        'font-size',
                                        data['font_size_title_call_back'])


def test_dw740(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                         'color',
                                         data['font_color_title_call_back_not_cursor'])


def test_dw741(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_background_color_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                               'background-color',
                                               data['background_color_btn_call_back_not_cursor'])


def test_dw742(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_background_color_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                               'background-image',
                                               data['background_color_btn_call_back_with_cursor'],
                                               1)


def test_dw743(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                         'color',
                                         data['font_color_title_call_back_with_cursor'],
                                         1)


def test_dw745(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_size_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'height',
                                   'width',
                                   data['height_btn_call_back'],
                                   data['width_call_back'])


def test_dw746(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.click_button(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                           BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS,
                           data['title_leave_contacts'])


def test_dw747(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.click_button_create_landing(FooterPageLocators.LOCATOR_CREATE_LANDING,
                                          FooterPageLocators.LOCATOR_VALIDATON_CREATE_LANDING,
                                          data['title_validation_landing'])


def test_dw748(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_CREATE_LANDING,
                                   data['title_btn_create_landing'])


def test_dw749(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_CREATE_LANDING,
                                   'font-family',
                                   data['font'])


def test_dw750(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_CREATE_LANDING,
                                        'font-size',
                                        data['font_size_title_create_landing'])


def test_dw751(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_CREATE_LANDING,
                                         'color',
                                         data['font_color_create_landing'])


def test_dw752(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.click_button(FooterPageLocators.LOCATOR_POLICY,
                           FooterPageLocators.LOCATOR_TITLE_POLICY_PAGE,
                           data['title_policy_page'])


def test_dw753(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_POLICY,
                                   data['title_btn_policy'])


def test_dw754(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_POLICY,
                                   'font-family',
                                   data['font'])


def test_dw755(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_POLICY,
                                        'font-size',
                                        data['font_size_title_policy'])


def test_dw756(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_POLICY,
                                         'color',
                                         data['font_color_policy'])


def test_dw757(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_name_button(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL,
                                   data['title_registration_symbol'])


def test_dw758(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_button(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL,
                                   'font-family',
                                   data['font'])


def test_dw759(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_size_button(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL,
                                        'font-size',
                                        data['font_size_registration_symbol'])


def test_dw760(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_font_color_button(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL,
                                         'color',
                                         data['font_color_registration_symbol'])


def test_dw761(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_favicon(FooterPageLocators.LOCATOR_FAVICON, 'favicon')


def test_dw762(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_type_cursor(FooterPageLocators.LOCATOR_BUTTON_RANSOM,
                                   'cursor',
                                   data['type_cursor_btn_ransom'])


def test_dw763(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_type_cursor(FooterPageLocators.LOCATOR_BUTTON_QUESTIONS_ANSWERS,
                                   'cursor',
                                   data['type_cursor_btn_questions_answers'])


def test_dw764(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_type_cursor(FooterPageLocators.LOCATOR_BUTTON_REVIEWS,
                                   'cursor',
                                   data['type_cursor_btn_reviews'])


def test_dw765(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_type_cursor(FooterPageLocators.LOCATOR_BUTTON_CALL,
                                   'cursor',
                                   data['type_cursor_btn_call'])


def test_dw766(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_type_cursor(FooterPageLocators.LOCATOR_BUTTON_CALL_BACK,
                                   'cursor',
                                   data['type_cursor_btn_call_back'])


def test_dw767(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_type_cursor(FooterPageLocators.LOCATOR_CREATE_LANDING,
                                   'cursor',
                                   data['type_cursor_create_landing'])


def test_dw768(browser):
    test_page = FooterPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FooterPageLocators.LOCATOR_REGISTERED_SYMBOL)
    time.sleep(2)
    test_page.checking_type_cursor(FooterPageLocators.LOCATOR_POLICY,
                                   'cursor',
                                   data['type_cursor_policy'])
