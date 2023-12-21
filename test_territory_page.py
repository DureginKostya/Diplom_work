import time
from pages.territory_page import TerritoryPage
from pages.locators import TerritoryPageLocators
import yaml


with open('data/testdata_territory.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw672(browser):
    contents = (TerritoryPageLocators.LOCATOR_TITLE, TerritoryPageLocators.LOCATOR_LIST_CITIES,
                TerritoryPageLocators.LOCATOR_TITLE_FIELD_PHONE, TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                TerritoryPageLocators.LOCATOR_BUTTON_SELL, TerritoryPageLocators.LOCATOR_TITLE_POLICY)
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw673(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(TerritoryPageLocators.LOCATOR_TITLE,
                                 data['title_territory'])


def test_dw674(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(TerritoryPageLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw675(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(TerritoryPageLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_territory'])


def test_dw676(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(TerritoryPageLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_title_territory'])


def test_dw677(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_list_cities(TerritoryPageLocators.LOCATOR_LIST_CITIES,
                                   data['list_cities'])


def test_dw678(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(TerritoryPageLocators.LOCATOR_LIST_CITIES,
                                 'font-family',
                                 data['font'])


def test_dw679(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(TerritoryPageLocators.LOCATOR_LIST_CITIES,
                                      'font-size',
                                      data['font_size_title_cities'])


def test_dw680(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(TerritoryPageLocators.LOCATOR_LIST_CITIES,
                                       'color',
                                       data['font_color_title_cities'])


def test_dw681(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(TerritoryPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                 data['title_field_phone'])


def test_dw682(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(TerritoryPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                 'font-family',
                                 data['font'])


def test_dw683(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(TerritoryPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                      'font-size',
                                      data['font_size_title_field_phone'])


def test_dw684(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(TerritoryPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                       'color',
                                       data['font_color_title_field_phone'])


def test_dw685(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                 data['title_btn_sell'])


def test_dw686(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                 'font-family',
                                 data['font'])


def test_dw687(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                      'font-size',
                                      data['font_size_title_btn_sell'])


def test_dw688(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                       'color',
                                       data['font_color_title_btn_sell'])


def test_dw689(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_background_color_button(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_not_cursor'])


def test_dw690(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_background_color_button(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_with_cursor'],
                                               1)


def test_dw691(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_size_button(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                   'height',
                                   'width',
                                   data['height_btn_sell'],
                                   data['width_btn_sell'])


def test_dw692(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_size_button(TerritoryPageLocators.LOCATOR_FIELD_PHONE_SIZE,
                                   'height',
                                   'width',
                                   data['height_field_phone'],
                                   data['width_field_phone'])


def test_dw693(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_placeholder_field_phone(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                               data['field_phone_text'])


def test_dw694(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text_field(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                       '+79999999999',
                                       'font-family',
                                       data['font'])


def test_dw695(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text_field(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                            '+79999999999',
                                            'font-size',
                                            data['font_size_field_phone_text'])


def test_dw696(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text_field(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                             '+79999999999',
                                             'color',
                                             data['font_color_field_phone_text'])


def test_dw697(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_background_color_field(TerritoryPageLocators.LOCATOR_FIELD_PHONE_SIZE,
                                              'background-color',
                                              data['background_color_field_phone'])


def test_dw698(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(TerritoryPageLocators.LOCATOR_TITLE_POLICY,
                                 data['title_btn_policy'])


def test_dw699(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(TerritoryPageLocators.LOCATOR_TITLE_POLICY,
                                 'font-family',
                                 data['font'])


def test_dw700(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(TerritoryPageLocators.LOCATOR_TITLE_POLICY,
                                      'font-size',
                                      data['font_size_title_btn_policy'])


def test_dw701(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(TerritoryPageLocators.LOCATOR_TITLE_POLICY,
                                       'color',
                                       data['font_color_title_btn_policy'])


def test_dw702(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.click_button(TerritoryPageLocators.LOCATOR_BUTTON_POLICY,
                           TerritoryPageLocators.LOCATOR_TITLE_POLICY_PAGE,
                           data['title_policy_page'])


def test_dw703(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                   'cursor',
                                   data['type_cursor_btn_sell'])


def test_dw704(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                   'cursor',
                                   data['type_cursor_field_phone_text'])


def test_dw705(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(TerritoryPageLocators.LOCATOR_BUTTON_POLICY,
                                   'cursor',
                                   data['type_cursor_btn_policy'])


def test_dw706(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                            data['test_data_positive_var1_field_phone'],
                                            TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                            TerritoryPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw707(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination1(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var1_field_phone'],
                                             TerritoryPageLocators.LOCATOR_BUTTON_SELL)


def test_dw708(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination2(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var2_field_phone'],
                                             TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                             TerritoryPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw709(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination3(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var3_field_phone'],
                                             TerritoryPageLocators.LOCATOR_BUTTON_SELL)


def test_dw710(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination3(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var4_field_phone'],
                                             TerritoryPageLocators.LOCATOR_BUTTON_SELL)


def test_dw711(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination3(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var5_field_phone'],
                                             TerritoryPageLocators.LOCATOR_BUTTON_SELL)


def test_dw712(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination4(TerritoryPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var6_field_phone'],
                                             TerritoryPageLocators.LOCATOR_BUTTON_SELL,
                                             TerritoryPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw713(browser):
    test_page = TerritoryPage(browser, data['url'])
    test_page.open_site()
    test_page.changed_window_size(1280, 728)
    test_page.go_to_element(TerritoryPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_scrolling_horizontal('list_cities')
    test_page.driver.maximize_window()
