from pages.karteka_or_other_page import KartekaOrOtherPage
from pages.locators import KartekaOrOtherPageLocators
import yaml


with open('data/testdata_karteka_or_other.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw323(browser):
    contents = (KartekaOrOtherPageLocators.LOCATOR_TITLE, KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_KARTEKA,
                KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_OTHER)
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_contents_page(contents)


def test_dw324(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_TITLE,
                                 data['title_karteka_or_other'])


def test_dw325(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw326(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_karteka_or_other'])


def test_dw327(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_title_karteka_or_other'])


def test_dw328(browser):
    contents = (KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_KARTEKA,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_1,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_2,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_2,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_4,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_5,
                KartekaOrOtherPageLocators.LOCATOR_ICON_SELLING_KARTEKA)
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_contents_page(contents)


def test_dw329(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_KARTEKA,
                                 data['title_selling_karteka'])


def test_dw330(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_KARTEKA,
                                 'font-family',
                                 data['font'])


def test_dw331(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_KARTEKA,
                                      'font-size',
                                      data['font_size_title_selling_karteka'])


def test_dw332(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_KARTEKA,
                                       'color',
                                       data['font_color_title_selling_karteka'])


def test_dw333(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_1,
                                 data['selling_karteka_paragraph_1'])


def test_dw334(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_1,
                                 'font-family',
                                 data['font'])


def test_dw335(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_1,
                                      'font-size',
                                      data['font_size_selling_karteka_paragraph_1'])


def test_dw336(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_1,
                                       'color',
                                       data['font_color_selling_karteka_paragraph_1'])


def test_dw337(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_2,
                                 data['selling_karteka_paragraph_2'])


def test_dw338(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_2,
                                 'font-family',
                                 data['font'])


def test_dw339(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_2,
                                      'font-size',
                                      data['font_size_selling_karteka_paragraph_2'])


def test_dw340(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_2,
                                       'color',
                                       data['font_color_selling_karteka_paragraph_2'])


def test_dw341(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_3,
                                 data['selling_karteka_paragraph_3'])


def test_dw342(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_3,
                                 'font-family',
                                 data['font'])


def test_dw343(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_3,
                                      'font-size',
                                      data['font_size_selling_karteka_paragraph_3'])


def test_dw344(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_3,
                                       'color',
                                       data['font_color_selling_karteka_paragraph_3'])


def test_dw345(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_4,
                                 data['selling_karteka_paragraph_4'])


def test_dw346(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_4,
                                 'font-family',
                                 data['font'])


def test_dw347(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_4,
                                      'font-size',
                                      data['font_size_selling_karteka_paragraph_4'])


def test_dw348(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_4,
                                       'color',
                                       data['font_color_selling_karteka_paragraph_4'])


def test_dw349(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_5,
                                 data['selling_karteka_paragraph_5'])


def test_dw350(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_5,
                                 'font-family',
                                 data['font'])


def test_dw351(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_5,
                                      'font-size',
                                      data['font_size_selling_karteka_paragraph_5'])


def test_dw352(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_KARTEKA_PARAGRAPH_5,
                                       'color',
                                       data['font_color_selling_karteka_paragraph_5'])


def test_dw353(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(KartekaOrOtherPageLocators.LOCATOR_ICON_SELLING_KARTEKA, data['title_icon_selling_karteka'])


def test_dw354(browser):
    contents = (KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_OTHER,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_1,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_2,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_3,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_4,
                KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_5,
                KartekaOrOtherPageLocators.LOCATOR_ICON_SELLING_OTHER)
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_contents_page(contents)


def test_dw355(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_OTHER,
                                 data['title_selling_other'])


def test_dw356(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_OTHER,
                                 'font-family',
                                 data['font'])


def test_dw357(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_OTHER,
                                      'font-size',
                                      data['font_size_title_selling_other'])


def test_dw358(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_TITLE_SELLING_OTHER,
                                       'color',
                                       data['font_color_title_selling_other'])


def test_dw359(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_1,
                                 data['selling_other_paragraph_1'])


def test_dw360(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_1,
                                 'font-family',
                                 data['font'])


def test_dw361(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_1,
                                      'font-size',
                                      data['font_size_selling_other_paragraph_1'])


def test_dw362(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_1,
                                       'color',
                                       data['font_color_selling_other_paragraph_1'])


def test_dw363(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_2,
                                 data['selling_other_paragraph_2'])


def test_dw364(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_2,
                                 'font-family',
                                 data['font'])


def test_dw365(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_2,
                                      'font-size',
                                      data['font_size_selling_other_paragraph_2'])


def test_dw366(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_2,
                                       'color',
                                       data['font_color_selling_other_paragraph_2'])


def test_dw367(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_3,
                                 data['selling_other_paragraph_3'])


def test_dw368(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_3,
                                 'font-family',
                                 data['font'])


def test_dw369(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_3,
                                      'font-size',
                                      data['font_size_selling_other_paragraph_3'])


def test_dw370(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_3,
                                       'color',
                                       data['font_color_selling_other_paragraph_3'])


def test_dw371(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_4,
                                 data['selling_other_paragraph_4'])


def test_dw372(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_4,
                                 'font-family',
                                 data['font'])


def test_dw373(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_4,
                                      'font-size',
                                      data['font_size_selling_other_paragraph_4'])


def test_dw374(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_4,
                                       'color',
                                       data['font_color_selling_other_paragraph_4'])


def test_dw375(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_name_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_5,
                                 data['selling_other_paragraph_5'])


def test_dw376(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_5,
                                 'font-family',
                                 data['font'])


def test_dw377(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_size_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_5,
                                      'font-size',
                                      data['font_size_selling_other_paragraph_5'])


def test_dw378(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(KartekaOrOtherPageLocators.LOCATOR_TITLE)
    test_page.checking_font_color_text(KartekaOrOtherPageLocators.LOCATOR_SELLING_OTHER_PARAGRAPH_5,
                                       'color',
                                       data['font_color_selling_other_paragraph_5'])


def test_dw379(browser):
    test_page = KartekaOrOtherPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(KartekaOrOtherPageLocators.LOCATOR_ICON_SELLING_OTHER, data['title_icon_selling_other'])
