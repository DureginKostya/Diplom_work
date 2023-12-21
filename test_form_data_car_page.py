import time
from pages.form_data_car_page import FormDateCarPage
from pages.locators import FormaDataCarLocators
import yaml

with open("data/testdata_form_data_car.yaml", encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw229(browser):
    contents = (FormaDataCarLocators.LOCATOR_TITLE, FormaDataCarLocators.LOCATOR_SUBTITLE,
                FormaDataCarLocators.LOCATOR_FIELD_BRAND, FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                FormaDataCarLocators.LOCATOR_FIELD_PHONE, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                FormaDataCarLocators.LOCATOR_TITLE_POLICY, FormaDataCarLocators.LOCATOR_BUTTON_POLICY,
                FormaDataCarLocators.LOCATOR_CHECKBOX_DTP, FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_DTP,
                FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN, FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BROKEN,
                FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT, FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_CREDIT,
                FormaDataCarLocators.LOCATOR_CHECKBOX_BAN, FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BAN)
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw230(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_TITLE,
                                 data['title_form_car_page'])


def test_dw231(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw232(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_form_car_page'])


def test_dw233(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_title_form_car_page'])


def test_dw234(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_SUBTITLE,
                                 data['subtitle_form_car_page'])


def test_dw235(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_SUBTITLE,
                                 'font-family',
                                 data['font'])


def test_dw236(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_SUBTITLE,
                                      'font-size',
                                      data['font_size_subtitle_form_car_page'])


def test_dw237(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_SUBTITLE,
                                       'color',
                                       data['font_color_subtitle_form_car_page'])


def test_dw238(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_size_button(FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                   'height',
                                   'width',
                                   data['height_field_brand_forma_car_page'],
                                   data['width_field_brand_forma_car_page'])


def test_dw239(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_placeholder_field(FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                         data['field_brand_text_form_car_page'])


def test_dw240(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text_field(FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                       'BMW M3',
                                       'font-family',
                                       data['font'])


def test_dw241(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text_field(FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                            'BMW M3',
                                            'font-size',
                                            data['font_size_field_brand_text_form_car_page'])


def test_dw242(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text_field(FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                             'BMW M3',
                                             'color',
                                             data['font_color_field_brand_text_form_car_page'])


def test_dw243(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_field(FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                              'background-color',
                                              data['background_color_field_brand_text_form_car_page'])


def test_dw244(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_size_button(FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                   'height',
                                   'width',
                                   data['height_field_year_forma_car_page'],
                                   data['width_field_year_forma_car_page'])


def test_dw245(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_placeholder_field(FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                         data['field_year_text_form_car_page'])


def test_dw246(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text_field(FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                       'BMW M3',
                                       'font-family',
                                       data['font'])


def test_dw247(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text_field(FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                            'BMW M3',
                                            'font-size',
                                            data['font_size_field_year_text_form_car_page'])


def test_dw248(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text_field(FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                             'BMW M3',
                                             'color',
                                             data['font_color_field_year_text_form_car_page'])


def test_dw249(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_background_color_field(FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                              'background-color',
                                              data['background_color_field_year_text_form_car_page'])


def test_dw250(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_size_button(FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                   'height',
                                   'width',
                                   data['height_field_phone_forma_car_page'],
                                   data['width_field_phone_forma_car_page'])


def test_dw251(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_placeholder_field(FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                         data['field_phone_text_form_car_page'])


def test_dw252(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text_field(FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                       'BMW M3',
                                       'font-family',
                                       data['font'])


def test_dw253(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text_field(FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                            'BMW M3',
                                            'font-size',
                                            data['font_size_field_phone_text_form_car_page'])


def test_dw254(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text_field(FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                             'BMW M3',
                                             'color',
                                             data['font_color_field_phone_text_form_car_page'])


def test_dw255(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_background_color_field(FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                              'background-color',
                                              data['background_color_field_phone_text_form_car_page'])


def test_dw256(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                 data['title_btn_sell_forms_car_page'])


def test_dw257(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                 'font-family',
                                 data['font'])


def test_dw258(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                      'font-size',
                                      data['font_size_title_btn_sell_forms_car_page'])


def test_dw259(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                       'color',
                                       data['font_color_title_btn_sell_forms_car_page'])


def test_dw260(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_background_color_button(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_forms_car_page_not_cursor'])


def test_dw261(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_background_color_button(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                               'background-image',
                                               data['background_color_btn_sell_forms_car_page_with_cursor'],
                                               1)


def test_dw262(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_size_button(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                   'height',
                                   'width',
                                   data['height_btn_sell_forms_car_page'],
                                   data['width_btn_sell_forms_car_page'])


def test_dw263(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_TITLE_POLICY,
                                 data['title_btn_policy_forma_car_page'])


def test_dw264(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_TITLE_POLICY,
                                 'font-family',
                                 data['font'])


def test_dw265(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_TITLE_POLICY,
                                      'font-size',
                                      data['font_size_title_btn_policy_forma_car_page'])


def test_dw266(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_TITLE_POLICY,
                                       'color',
                                       data['font_color_title_btn_policy_forma_car_page'])


def test_dw267(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.click_button(FormaDataCarLocators.LOCATOR_BUTTON_POLICY,
                           FormaDataCarLocators.LOCATOR_TITLE_POLICY_PAGE,
                           data['title_policy_page'])


def test_dw268(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_DTP,
                                 data['title_checkbox_dtp_forms_car_page'])


def test_dw269(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_DTP,
                                 'font-family',
                                 data['font'])


def test_dw270(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_DTP,
                                      'font-size',
                                      data['font_size_title_checkbox_dtp_forms_car_page'])


def test_dw271(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_DTP,
                                       'color',
                                       data['font_color_title_checkbox_dtp_forms_car_page'])


def test_dw272(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BROKEN,
                                 data['title_checkbox_broken_forms_car_page'])


def test_dw273(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BROKEN,
                                 'font-family',
                                 data['font'])


def test_dw274(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BROKEN,
                                      'font-size',
                                      data['font_size_title_checkbox_broken_forms_car_page'])


def test_dw275(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BROKEN,
                                       'color',
                                       data['font_color_title_checkbox_broken_forms_car_page'])


def test_dw276(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_CREDIT,
                                 data['title_checkbox_credit_forms_car_page'])


def test_dw277(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_CREDIT,
                                 'font-family',
                                 data['font'])


def test_dw278(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_CREDIT,
                                      'font-size',
                                      data['font_size_title_checkbox_credit_forms_car_page'])


def test_dw279(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_CREDIT,
                                       'color',
                                       data['font_color_title_checkbox_credit_forms_car_page'])


def test_dw280(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BAN,
                                 data['title_checkbox_ban_forms_car_page'])


def test_dw281(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BAN,
                                 'font-family',
                                 data['font'])


def test_dw282(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BAN,
                                      'font-size',
                                      data['font_size_title_checkbox_ban_forms_car_page'])


def test_dw283(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BAN,
                                       'color',
                                       data['font_color_title_checkbox_ban_forms_car_page'])


def test_dw288(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                   'cursor',
                                   data['type_cursor_field_brand_forms_car_page'])


def test_dw289(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                   'cursor',
                                   data['type_cursor_field_year_forms_car_page'])


def test_dw290(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                   'cursor',
                                   data['type_cursor_field_phone_forms_car_page'])


def test_dw291(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                   'cursor',
                                   data['type_cursor_btn_sell_forms_car_page'])


def test_dw292(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_BUTTON_POLICY,
                                   'cursor',
                                   data['type_cursor_btn_policy_forms_car_page'])


def test_dw293(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_DTP,
                                   'cursor',
                                   data['type_cursor_checkbox_dtp_forms_car_page'])


def test_dw294(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BROKEN,
                                   'cursor',
                                   data['type_cursor_checkbox_broken_forms_car_page'])


def test_dw295(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_CREDIT,
                                   'cursor',
                                   data['type_cursor_checkbox_credit_forms_car_page'])


def test_dw296(browser):
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_type_cursor(FormaDataCarLocators.LOCATOR_TITLE_CHECKBOX_BAN,
                                   'cursor',
                                   data['type_cursor_checkbox_ban_forms_car_page'])


def test_dw297(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var1_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var1_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var1_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var1_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var1_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var1_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var1_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw298(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var2_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var2_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var2_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var2_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var2_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var2_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var2_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw299(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var3_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var3_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var3_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var3_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var3_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var3_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var3_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw300(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var4_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var4_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var4_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var4_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var4_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var4_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var4_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw301(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var5_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var5_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var5_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var5_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var5_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var5_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var5_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw302(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var6_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var6_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var6_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var6_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var6_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var6_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var6_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw303(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var7_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var7_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var7_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var7_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var7_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var7_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var7_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw304(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var8_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var8_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var8_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var8_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var8_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var8_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var8_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw305(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var9_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var9_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var9_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var9_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var9_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var9_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var9_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw306(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var10_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var10_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var10_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var10_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var10_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var10_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var10_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw307(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var11_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var11_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var11_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var11_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var11_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var11_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var11_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw308(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var12_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var12_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var12_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var12_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var12_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var12_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var12_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw309(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var13_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var13_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var13_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var13_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var13_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var13_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var13_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw310(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_positive_var14_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_positive_var14_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_positive_var14_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_positive_var14_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_positive_var14_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_positive_var14_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_positive_var14_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_positive_examination(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                            FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                            data['title_thank_you_page'])


def test_dw311(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var1_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var1_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var1_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var1_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var1_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var1_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var1_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_BRAND)


def test_dw312(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var2_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var2_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var2_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var2_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var2_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var2_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var2_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination2(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_BRAND,
                                             FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw313(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var3_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var3_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var3_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var3_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var3_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var3_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var3_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination3(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                             FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw314(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var4_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var4_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var4_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var4_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var4_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var4_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var4_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination4(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                             FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw315(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var5_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var5_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var5_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var5_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var5_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var5_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var5_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination3(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                             FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw316(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var6_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var6_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var6_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var6_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var6_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var6_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var6_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination3(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_YEAR,
                                             FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw317(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var7_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var7_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var7_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var7_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var7_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var7_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var7_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination5(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_PHONE)


def test_dw318(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var8_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var8_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var8_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var8_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var8_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var8_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var8_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination6(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                             FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])


def test_dw319(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var9_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var9_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var9_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var9_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var9_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var9_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var9_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination7(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_BRAND)


def test_dw320(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var10_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var10_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var10_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var10_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var10_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var10_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var10_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_YEAR)


def test_dw321(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var11_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var11_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var11_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var11_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var11_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var11_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var11_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination1(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_PHONE)


def test_dw322(browser):
    dict_fld = {FormaDataCarLocators.LOCATOR_FIELD_BRAND: data['td_negative_var12_field_brand_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_YEAR: data['td_negative_var12_field_year_forms_car_page'],
                FormaDataCarLocators.LOCATOR_FIELD_PHONE: data['td_negative_var12_field_phone_forms_car_page']}
    dict_cb = {FormaDataCarLocators.LOCATOR_CHECKBOX_DTP: data['td_negative_var12_checked_dtp_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BROKEN: data['td_negative_var12_checked_broken_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_CREDIT: data['td_negative_var12_checked_credit_forms_car_page'],
               FormaDataCarLocators.LOCATOR_CHECKBOX_BAN: data['td_negative_var12_checked_ban_forms_car_page']}
    test_page = FormDateCarPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(FormaDataCarLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_negative_examination8(dict_fld, dict_cb, FormaDataCarLocators.LOCATOR_BUTTON_SELL,
                                             FormaDataCarLocators.LOCATOR_FIELD_PHONE,
                                             FormaDataCarLocators.LOCATOR_TITLE_THANK_YOU_PAGE,
                                             data['title_thank_you_page'])
