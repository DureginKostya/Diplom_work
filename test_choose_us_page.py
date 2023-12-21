from pages.choose_us_page import ChooseUsPage
from pages.locators import ChooseUsPageLocators
import yaml


with open('data/testdata_choose_us.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw128(browser):
    contents = (ChooseUsPageLocators.LOCATOR_TITLE, ChooseUsPageLocators.LOCATOR_EXPLANATION,
                ChooseUsPageLocators.LOCATOR_TITLE_BEST_PRICE, ChooseUsPageLocators.LOCATOR_TITLE_FREE_SUPPORT,
                ChooseUsPageLocators.LOCATOR_TITLE_ALL_MONEY)
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_contents_page(contents)


def test_dw129(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_TITLE,
                                 data['title_choose_us'])


def test_dw130(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw131(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_choose_us'])


def test_dw132(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_registration_symbol'])


def test_dw133(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_EXPLANATION,
                                 data['explanation_choose_us'])


def test_dw134(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_EXPLANATION,
                                 'font-family',
                                 data['font'])


def test_dw135(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_EXPLANATION,
                                      'font-size',
                                      data['font_size_explanation_choose_us'])


def test_dw136(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_EXPLANATION,
                                       'color',
                                       data['font_color_explanation_choose_us'])


def test_dw137(browser):
    contents = (ChooseUsPageLocators.LOCATOR_TITLE_BEST_PRICE, ChooseUsPageLocators.LOCATOR_DESCRIPTION_BEST_PRICE,
                ChooseUsPageLocators.LOCATOR_ICON_BEST_PRICE)
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_contents_page(contents)


def test_dw138(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_TITLE_BEST_PRICE,
                                 data['title_best_price'])


def test_dw139(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_TITLE_BEST_PRICE,
                                 'font-family',
                                 data['font'])


def test_dw140(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_TITLE_BEST_PRICE,
                                      'font-size',
                                      data['font_size_title_best_price'])


def test_dw141(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_TITLE_BEST_PRICE,
                                       'color',
                                       data['font_color_title_best_price'])


def test_dw142(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_BEST_PRICE,
                                 data['description_best_price'])


def test_dw143(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_BEST_PRICE,
                                 'font-family',
                                 data['font'])


def test_dw144(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_BEST_PRICE,
                                      'font-size',
                                      data['font_size_description_best_price'])


def test_dw145(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_BEST_PRICE,
                                       'color',
                                       data['font_color_description_best_price'])


def test_dw146(browser):
    contents = (ChooseUsPageLocators.LOCATOR_TITLE_FREE_SUPPORT, ChooseUsPageLocators.LOCATOR_DESCRIPTION_FREE_SUPPORT,
                ChooseUsPageLocators.LOCATOR_ICON_FREE_SUPPORT)
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_contents_page(contents)


def test_dw147(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_TITLE_FREE_SUPPORT,
                                 data['title_free_support'])


def test_dw148(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_TITLE_FREE_SUPPORT,
                                 'font-family',
                                 data['font'])


def test_dw149(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_TITLE_FREE_SUPPORT,
                                      'font-size',
                                      data['font_size_title_free_support'])


def test_dw150(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_TITLE_FREE_SUPPORT,
                                       'color',
                                       data['font_color_title_free_support'])


def test_dw151(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_FREE_SUPPORT,
                                 data['description_free_support'])


def test_dw152(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_FREE_SUPPORT,
                                 'font-family',
                                 data['font'])


def test_dw153(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_FREE_SUPPORT,
                                      'font-size',
                                      data['font_size_description_free_support'])


def test_dw154(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_FREE_SUPPORT,
                                       'color',
                                       data['font_color_description_free_support'])


def test_dw155(browser):
    contents = (ChooseUsPageLocators.LOCATOR_TITLE_ALL_MONEY, ChooseUsPageLocators.LOCATOR_DESCRIPTION_ALL_MONEY,
                ChooseUsPageLocators.LOCATOR_ICON_ALL_MONEY)
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_contents_page(contents)


def test_dw156(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_TITLE_ALL_MONEY,
                                 data['title_all_money'])


def test_dw157(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_TITLE_ALL_MONEY,
                                 'font-family',
                                 data['font'])


def test_dw158(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_TITLE_ALL_MONEY,
                                      'font-size',
                                      data['font_size_title_all_money'])


def test_dw159(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_TITLE_ALL_MONEY,
                                       'color',
                                       data['font_color_title_all_money'])


def test_dw160(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_ALL_MONEY,
                                 data['description_all_money'])


def test_dw161(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_ALL_MONEY,
                                 'font-family',
                                 data['font'])


def test_dw162(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_ALL_MONEY,
                                      'font-size',
                                      data['font_size_description_all_money'])


def test_dw163(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ChooseUsPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(ChooseUsPageLocators.LOCATOR_DESCRIPTION_ALL_MONEY,
                                       'color',
                                       data['font_color_description_all_money'])


def test_dw164(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(ChooseUsPageLocators.LOCATOR_ICON_BEST_PRICE, data['title_icon_best_price'])


def test_dw165(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(ChooseUsPageLocators.LOCATOR_ICON_FREE_SUPPORT, data['title_icon_free_support'])


def test_dw166(browser):
    test_page = ChooseUsPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(ChooseUsPageLocators.LOCATOR_ICON_ALL_MONEY, data['title_icon_all_money'])
