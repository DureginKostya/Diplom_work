from pages.main_page import MainPage
from pages.locators import MainPageLocators
import yaml

with open("data/testdata_main.yaml", encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw73(browser):
    contents = (MainPageLocators.LOCATOR_TITLE, MainPageLocators.LOCATOR_SUBTITLE,
                MainPageLocators.LOCATOR_BENEFITS_URGENTLY, MainPageLocators.LOCATOR_BENEFITS_EXPENSIVE,
                MainPageLocators.LOCATOR_BENEFITS_AROUND_CLOCK, MainPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                MainPageLocators.LOCATOR_FIELD_PHONE, MainPageLocators.LOCATOR_BUTTON_SELL,
                MainPageLocators.LOCATOR_TITLE_POLICY, MainPageLocators.LOCATOR_BUTTON_POLICY)
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_contents_page(contents)


def test_dw74(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_TITLE,
                                 data['title_main_page'])


def test_dw75(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw76(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_main_page'])


def test_dw77(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_title_main_page'])


def test_dw78(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_SUBTITLE,
                                 data['subtitle_main_page'])


def test_dw79(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_SUBTITLE,
                                 'font-family',
                                 data['font'])


def test_dw80(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_SUBTITLE,
                                      'font-size',
                                      data['font_size_subtitle_main_page'])


def test_dw81(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_SUBTITLE,
                                       'color',
                                       data['font_color_subtitle_main_page'])


def test_dw82(browser):
    contents = (MainPageLocators.LOCATOR_BENEFITS_URGENTLY, MainPageLocators.LOCATOR_BENEFITS_EXPENSIVE,
                MainPageLocators.LOCATOR_BENEFITS_AROUND_CLOCK)
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_contents_page(contents)


def test_dw83(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_BENEFITS_URGENTLY,
                                 data['benefits_urgently_main_page'])


def test_dw84(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_BENEFITS_URGENTLY,
                                 'font-family',
                                 data['font'])


def test_dw85(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_BENEFITS_URGENTLY,
                                      'font-size',
                                      data['font_size_benefits_urgently_main_page'])


def test_dw86(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_BENEFITS_URGENTLY,
                                       'color',
                                       data['font_color_benefits_urgently_main_page'])


def test_dw87(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_BENEFITS_EXPENSIVE,
                                 data['benefits_expensive_main_page'])


def test_dw88(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_BENEFITS_EXPENSIVE,
                                 'font-family',
                                 data['font'])


def test_dw89(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_BENEFITS_EXPENSIVE,
                                      'font-size',
                                      data['font_size_benefits_expensive_main_page'])


def test_dw90(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_BENEFITS_EXPENSIVE,
                                       'color',
                                       data['font_color_benefits_expensive_main_page'])


def test_dw91(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_BENEFITS_AROUND_CLOCK,
                                 data['benefits_around_clock_main_page'])


def test_dw92(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_BENEFITS_AROUND_CLOCK,
                                 'font-family',
                                 data['font'])


def test_dw93(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_BENEFITS_AROUND_CLOCK,
                                      'font-size',
                                      data['font_size_benefits_around_clock_main_page'])


def test_dw94(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_BENEFITS_AROUND_CLOCK,
                                       'color',
                                       data['font_color_benefits_around_clock_main_page'])


def test_dw95(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                 data['title_field_phone_main_page'])


def test_dw96(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                 'font-family',
                                 data['font'])


def test_dw97(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                      'font-size',
                                      data['font_size_title_field_phone_main_page'])


def test_dw98(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                       'color',
                                       data['font_color_title_field_phone_main_page'])


def test_dw99(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_BUTTON_SELL,
                                 data['title_btn_sell_main_page'])


def test_dw100(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_BUTTON_SELL,
                                 'font-family',
                                 data['font'])


def test_dw101(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_BUTTON_SELL,
                                      'font-size',
                                      data['font_size_title_btn_sell_main_page'])


def test_dw102(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_BUTTON_SELL,
                                       'color',
                                       data['font_color_title_btn_sell_main_page'])


def test_dw103(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_button(MainPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_main_page_not_cursor'])


def test_dw104(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_button(MainPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_main_page_with_cursor'],
                                               1)


def test_dw105(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_size_button(MainPageLocators.LOCATOR_BUTTON_SELL,
                                   'height',
                                   'width',
                                   data['height_btn_sell_main_page'],
                                   data['width_btn_sell_main_page'])


def test_dw106(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_size_button(MainPageLocators.LOCATOR_FIELD_PHONE_SIZE,
                                   'height',
                                   'width',
                                   data['height_field_phone_main_page'],
                                   data['width_field_phone_main_page'])


def test_dw107(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_placeholder_field_phone(MainPageLocators.LOCATOR_FIELD_PHONE,
                                               data['field_phone_text_main_page'])


def test_dw108(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text_field(MainPageLocators.LOCATOR_FIELD_PHONE,
                                       '+79999999999',
                                       'font-family',
                                       data['font'])


def test_dw109(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text_field(MainPageLocators.LOCATOR_FIELD_PHONE,
                                            '+79999999999',
                                            'font-size',
                                            data['font_size_field_phone_text_main_page'])


def test_dw110(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text_field(MainPageLocators.LOCATOR_FIELD_PHONE,
                                             '+79999999999',
                                             'color',
                                             data['font_color_field_phone_text_main_page'])


def test_dw112(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_field(MainPageLocators.LOCATOR_FIELD_PHONE_SIZE,
                                              'background-color',
                                              data['background_color_field_phone_main_page'])


def test_dw113(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_name_text(MainPageLocators.LOCATOR_TITLE_POLICY,
                                 data['title_btn_policy_main_page'])


def test_dw114(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_text(MainPageLocators.LOCATOR_TITLE_POLICY,
                                 'font-family',
                                 data['font'])


def test_dw115(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_size_text(MainPageLocators.LOCATOR_TITLE_POLICY,
                                      'font-size',
                                      data['font_size_title_btn_policy_main_page'])


def test_dw116(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_font_color_text(MainPageLocators.LOCATOR_TITLE_POLICY,
                                       'color',
                                       data['font_color_title_btn_policy_main_page'])


def test_dw117(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.click_button(MainPageLocators.LOCATOR_BUTTON_POLICY,
                           MainPageLocators.LOCATOR_TITLE_POLICY_PAGE,
                           data['title_policy_page'])


def test_dw118(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(MainPageLocators.LOCATOR_BUTTON_SELL,
                                   'cursor',
                                   data['type_cursor_btn_sell_main_page'])


def test_dw119(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(MainPageLocators.LOCATOR_FIELD_PHONE,
                                   'cursor',
                                   data['type_cursor_field_phone_text_main_page'])


def test_dw120(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_type_cursor(MainPageLocators.LOCATOR_BUTTON_POLICY,
                                   'cursor',
                                   data['type_cursor_policy'])


def test_dw121(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_positive_examination(MainPageLocators.LOCATOR_FIELD_PHONE,
                                            data['test_data_positive_var1_field_phone'],
                                            MainPageLocators.LOCATOR_BUTTON_SELL,
                                            MainPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw122(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_negative_examination1(MainPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var1_field_phone'],
                                             MainPageLocators.LOCATOR_BUTTON_SELL)


def test_dw123(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_negative_examination2(MainPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var2_field_phone'],
                                             MainPageLocators.LOCATOR_BUTTON_SELL,
                                             MainPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw124(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_negative_examination3(MainPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var3_field_phone'],
                                             MainPageLocators.LOCATOR_BUTTON_SELL)


def test_dw125(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_negative_examination3(MainPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var4_field_phone'],
                                             MainPageLocators.LOCATOR_BUTTON_SELL)


def test_dw126(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_negative_examination3(MainPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var5_field_phone'],
                                             MainPageLocators.LOCATOR_BUTTON_SELL)


def test_dw127(browser):
    test_page = MainPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_negative_examination4(MainPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var6_field_phone'],
                                             MainPageLocators.LOCATOR_BUTTON_SELL,
                                             MainPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])
