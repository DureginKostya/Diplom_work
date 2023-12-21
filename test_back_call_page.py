import time
from pages.back_call_page import BackCallPage
from pages.locators import BackCallPageLocators, HeaderPageLocators
import yaml


with open('data/testdata_back_call.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw769(browser):
    contents = (BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS, BackCallPageLocators.LOCATOR_SUBTITLE_LEAVE_CONTACTS,
                BackCallPageLocators.LOCATOR_FIELD_NAME, BackCallPageLocators.LOCATOR_FIELD_PHONE,
                BackCallPageLocators.LOCATOR_BUTTON_SELL, BackCallPageLocators.LOCATOR_TITLE_POLICY)
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw770(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_name_text(BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS,
                                 data['title_back_call'])


def test_dw771(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_text(BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS,
                                 'font-family',
                                 data['font'])


def test_dw772(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_size_text(BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS,
                                      'font-size',
                                      data['font_size_title_back_call'])


def test_dw773(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_color_text(BackCallPageLocators.LOCATOR_TITLE_LEAVE_CONTACTS,
                                       'color',
                                       data['font_color_title_back_call'])


def test_dw774(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_name_text(BackCallPageLocators.LOCATOR_SUBTITLE_LEAVE_CONTACTS,
                                 data['subtitle_back_call'])


def test_dw775(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_text(BackCallPageLocators.LOCATOR_SUBTITLE_LEAVE_CONTACTS,
                                 'font-family',
                                 data['font'])


def test_dw776(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_size_text(BackCallPageLocators.LOCATOR_SUBTITLE_LEAVE_CONTACTS,
                                      'font-size',
                                      data['font_size_subtitle_back_call'])


def test_dw777(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_color_text(BackCallPageLocators.LOCATOR_SUBTITLE_LEAVE_CONTACTS,
                                       'color',
                                       data['font_color_subtitle_back_call'])


def test_dw778(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_size_button(BackCallPageLocators.LOCATOR_FIELD_NAME,
                                   'height',
                                   'width',
                                   data['height_field_name'],
                                   data['width_field_name'])


def test_dw779(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_placeholder(BackCallPageLocators.LOCATOR_FIELD_NAME,
                                   data['field_name_text'])


def test_dw780(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_text_field(BackCallPageLocators.LOCATOR_FIELD_NAME,
                                       'Александр',
                                       'font-family',
                                       data['font'])


def test_dw781(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_size_text_field(BackCallPageLocators.LOCATOR_FIELD_NAME,
                                            'Александр',
                                            'font-size',
                                            data['font_size_field_name_text'])


def test_dw782(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_color_text_field(BackCallPageLocators.LOCATOR_FIELD_NAME,
                                             'Александр',
                                             'color',
                                             data['font_color_field_name_text'])


def test_dw783(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_background_color_field(BackCallPageLocators.LOCATOR_FIELD_NAME,
                                              'background-color',
                                              data['background_color_name_phone'])


def test_dw784(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_size_button(BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                   'height',
                                   'width',
                                   data['height_field_phone'],
                                   data['width_field_phone'])


def test_dw785(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_placeholder(BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                   data['field_phone_text'])


def test_dw786(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_text_field(BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                       '+79999999999',
                                       'font-family',
                                       data['font'])


def test_dw787(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_size_text_field(BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                            '+79999999999',
                                            'font-size',
                                            data['font_size_field_phone_text'])


def test_dw788(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_color_text_field(BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                             '+79999999999',
                                             'color',
                                             data['font_color_field_phone_text'])


def test_dw789(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_background_color_field(BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                              'background-color',
                                              data['background_color_field_phone'])


def test_dw790(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_name_text(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                 data['title_btn_sell'])


def test_dw791(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_text(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                 'font-family',
                                 data['font'])


def test_dw792(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_size_text(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                      'font-size',
                                      data['font_size_title_btn_sell'])


def test_dw793(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_color_text(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                       'color',
                                       data['font_color_title_btn_sell'])


def test_dw794(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_background_color_button(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_not_cursor'])


def test_dw795(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_background_color_button(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_with_cursor'],
                                               1)


def test_dw796(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_size_button(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                   'height',
                                   'width',
                                   data['height_btn_sell'],
                                   data['width_btn_sell'])


def test_dw797(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_name_text(BackCallPageLocators.LOCATOR_TITLE_POLICY,
                                 data['title_btn_policy'])


def test_dw798(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_text(BackCallPageLocators.LOCATOR_TITLE_POLICY,
                                 'font-family',
                                 data['font'])


def test_dw799(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_size_text(BackCallPageLocators.LOCATOR_TITLE_POLICY,
                                      'font-size',
                                      data['font_size_title_btn_policy'])


def test_dw800(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_font_color_text(BackCallPageLocators.LOCATOR_TITLE_POLICY,
                                       'color',
                                       data['font_color_title_btn_policy'])


def test_dw801(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.click_button(BackCallPageLocators.LOCATOR_BUTTON_POLICY,
                           BackCallPageLocators.LOCATOR_TITLE_POLICY_PAGE,
                           data['title_policy_page'])


def test_dw802(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_type_cursor(BackCallPageLocators.LOCATOR_FIELD_NAME,
                                   'cursor',
                                   data['type_cursor_field_name_text'])


def test_dw803(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_type_cursor(BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                   'cursor',
                                   data['type_cursor_field_phone_text'])


def test_dw804(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_type_cursor(BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                   'cursor',
                                   data['type_cursor_btn_sell'])


def test_dw805(browser):
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_type_cursor(BackCallPageLocators.LOCATOR_BUTTON_POLICY,
                                   'cursor',
                                   data['type_cursor_btn_policy'])


def test_dw806(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_positive_var1_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_positive_var1_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                            BackCallPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw807(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_positive_var2_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_positive_var2_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                            BackCallPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw808(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_positive_var3_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_positive_var3_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                            BackCallPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw809(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var1_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var1_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_NAME)


def test_dw810(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var3_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var3_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination3(dict_fld,  BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_PHONE)


def test_dw811(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var2_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var2_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination2(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_NAME,
                                             BackCallPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw812(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var4_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var4_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination4(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                             BackCallPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw813(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var5_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var5_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_NAME)


def test_dw814(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var6_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var6_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_NAME)


def test_dw815(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var7_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var7_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_NAME)


def test_dw816(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var8_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var8_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_PHONE)


def test_dw817(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var9_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var9_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_PHONE)


def test_dw818(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var10_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var10_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_PHONE)


def test_dw819(browser):
    dict_fld = {BackCallPageLocators.LOCATOR_FIELD_NAME: data['td_negative_var11_field_name'],
                BackCallPageLocators.LOCATOR_FIELD_PHONE: data['td_negative_var11_field_phone']}
    test_page = BackCallPage(browser, data['url'])
    test_page.open_site()
    test_page.open_window_back_call(HeaderPageLocators.LOCATOR_BUTTON_CALL_BACK)
    time.sleep(2)
    test_page.checking_negative_examination5(dict_fld, BackCallPageLocators.LOCATOR_BUTTON_SELL,
                                             BackCallPageLocators.LOCATOR_FIELD_PHONE,
                                             BackCallPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])
