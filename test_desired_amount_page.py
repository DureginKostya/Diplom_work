import time
from pages.desired_amount_page import DesiredAmountPage
from pages.locators import DesiredAmountPageLocators
import yaml


with open('data/testdata_desired_amount.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw380(browser):
    contents = (DesiredAmountPageLocators.LOCATOR_TITLE, DesiredAmountPageLocators.LOCATOR_QUESTION_1,
                DesiredAmountPageLocators.LOCATOR_ANSWER_1, DesiredAmountPageLocators.LOCATOR_QUESTION_2,
                DesiredAmountPageLocators.LOCATOR_ANSWER_2, DesiredAmountPageLocators.LOCATOR_NOTE,
                DesiredAmountPageLocators.LOCATOR_ICON_NOTE, DesiredAmountPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                DesiredAmountPageLocators.LOCATOR_FIELD_PHONE, DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                DesiredAmountPageLocators.LOCATOR_TITLE_POLICY)
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw381(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_TITLE,
                                 data['title_desired_amount'])


def test_dw382(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw383(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_desired_amount'])


def test_dw384(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_title_desired_amount'])


def test_dw385(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_QUESTION_1,
                                 data['title_question_1'])


def test_dw386(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_QUESTION_1,
                                 'font-family',
                                 data['font'])


def test_dw387(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_QUESTION_1,
                                      'font-size',
                                      data['font_size_title_question_1'])


def test_dw388(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_QUESTION_1,
                                       'color',
                                       data['font_color_title_question_1'])


def test_dw389(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_ANSWER_1,
                                 data['title_answer_1'])


def test_dw390(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_ANSWER_1,
                                 'font-family',
                                 data['font'])


def test_dw391(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_ANSWER_1,
                                      'font-size',
                                      data['font_size_title_answer_1'])


def test_dw392(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_ANSWER_1,
                                       'color',
                                       data['font_color_title_answer_1'])


def test_dw393(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_QUESTION_2,
                                 data['title_question_2'])


def test_dw394(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_QUESTION_2,
                                 'font-family',
                                 data['font'])


def test_dw395(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_QUESTION_2,
                                      'font-size',
                                      data['font_size_title_question_2'])


def test_dw396(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_QUESTION_2,
                                       'color',
                                       data['font_color_title_question_2'])


def test_dw397(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_ANSWER_2,
                                 data['title_answer_2'])


def test_dw398(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_ANSWER_2,
                                 'font-family',
                                 data['font'])


def test_dw399(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_ANSWER_2,
                                      'font-size',
                                      data['font_size_title_answer_2'])


def test_dw400(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_ANSWER_2,
                                       'color',
                                       data['font_color_title_answer_2'])


def test_dw401(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_NOTE,
                                 data['title_note'])


def test_dw402(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_NOTE,
                                 'font-family',
                                 data['font'])


def test_dw403(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_NOTE,
                                      'font-size',
                                      data['font_size_title_note'])


def test_dw404(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_NOTE,
                                       'color',
                                       data['font_color_title_note'])


def test_dw405(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(DesiredAmountPageLocators.LOCATOR_ICON_NOTE,
                            data['title_icon_note'])


def test_dw407(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                 data['title_field_phone'])


def test_dw408(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                 'font-family',
                                 data['font'])


def test_dw409(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                      'font-size',
                                      data['font_size_title_field_phone'])


def test_dw410(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_TITLE_FIELD_PHONE,
                                       'color',
                                       data['font_color_title_field_phone'])


def test_dw411(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                 data['title_btn_sell'])


def test_dw412(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                 'font-family',
                                 data['font'])


def test_dw413(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                      'font-size',
                                      data['font_size_title_btn_sell'])


def test_dw414(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                       'color',
                                       data['font_color_title_btn_sell'])


def test_dw415(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_background_color_button(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_not_cursor'])


def test_dw416(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_background_color_button(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_with_cursor'],
                                               1)


def test_dw417(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_size_button(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                   'height',
                                   'width',
                                   data['height_btn_sell'],
                                   data['width_btn_sell'])


def test_dw418(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_size_button(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE_SIZE,
                                   'height',
                                   'width',
                                   data['height_field_phone'],
                                   data['width_field_phone'])


def test_dw419(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_placeholder_field_phone(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                               data['field_phone_text'])


def test_dw420(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_text_field(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                       '+79999999999',
                                       'font-family',
                                       data['font'])


def test_dw421(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text_field(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                            '+79999999999',
                                            'font-size',
                                            data['font_size_field_phone_text'])


def test_dw422(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text_field(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                             '+79999999999',
                                             'color',
                                             data['font_color_field_phone_text'])


def test_dw423(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_background_color_field(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE_SIZE,
                                              'background-color',
                                              data['background_color_field_phone'])


def test_dw424(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_name_text(DesiredAmountPageLocators.LOCATOR_TITLE_POLICY,
                                 data['title_btn_policy'])


def test_dw425(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_text(DesiredAmountPageLocators.LOCATOR_TITLE_POLICY,
                                 'font-family',
                                 data['font'])


def test_dw426(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(DesiredAmountPageLocators.LOCATOR_TITLE_POLICY,
                                      'font-size',
                                      data['font_size_title_btn_policy'])


def test_dw427(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(DesiredAmountPageLocators.LOCATOR_TITLE_POLICY,
                                       'color',
                                       data['font_color_title_btn_policy'])


def test_dw428(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.click_button(DesiredAmountPageLocators.LOCATOR_BUTTON_POLICY,
                           DesiredAmountPageLocators.LOCATOR_TITLE_POLICY_PAGE,
                           data['title_policy_page'])


def test_dw429(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_type_cursor(DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                   'cursor',
                                   data['type_cursor_btn_sell'])


def test_dw430(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_type_cursor(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                   'cursor',
                                   data['type_cursor_field_phone_text'])


def test_dw431(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_type_cursor(DesiredAmountPageLocators.LOCATOR_BUTTON_POLICY,
                                   'cursor',
                                   data['type_cursor_btn_policy'])


def test_dw432(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_positive_examination(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                            data['test_data_positive_var1_field_phone'],
                                            DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                            DesiredAmountPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw433(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_negative_examination1(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var1_field_phone'],
                                             DesiredAmountPageLocators.LOCATOR_BUTTON_SELL)


def test_dw434(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_negative_examination2(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var2_field_phone'],
                                             DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                             DesiredAmountPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw435(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_negative_examination3(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var3_field_phone'],
                                             DesiredAmountPageLocators.LOCATOR_BUTTON_SELL)


def test_dw436(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_negative_examination3(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var4_field_phone'],
                                             DesiredAmountPageLocators.LOCATOR_BUTTON_SELL)


def test_dw437(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_negative_examination3(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var5_field_phone'],
                                             DesiredAmountPageLocators.LOCATOR_BUTTON_SELL)


def test_dw438(browser):
    test_page = DesiredAmountPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(DesiredAmountPageLocators.LOCATOR_NAVIGATION_PAGE)
    time.sleep(2)
    test_page.checking_negative_examination4(DesiredAmountPageLocators.LOCATOR_FIELD_PHONE,
                                             data['test_data_negative_var6_field_phone'],
                                             DesiredAmountPageLocators.LOCATOR_BUTTON_SELL,
                                             DesiredAmountPageLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])
