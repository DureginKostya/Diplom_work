import time
from pages.ransom_all_page import RansomAllPage
from pages.locators import RansomAllPageLocators
import yaml


with open('data/testdata_ransom_all.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw167(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_NEW_OLD,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PREMIUM, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_BROKEN,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_CREDIT, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_EMERGENCY,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_DUPLICATE_PTS,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_ARRESTED, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PROBLEM)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw169(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE,
                                 data['title_ransom_all'])


def test_dw170(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE,
                                 'font-family',
                                 data['font'])


def test_dw171(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE,
                                      'font-size',
                                      data['font_size_title_ransom_all'])


def test_dw172(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE,
                                       'color',
                                       data['font_color_title_ransom_all'])


def test_dw173(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_NEW_OLD, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_NEW_OLD)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw174(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_NEW_OLD,
                                 data['title_block_new_old'])


def test_dw175(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_NEW_OLD,
                                 'font-family',
                                 data['font'])


def test_dw176(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_NEW_OLD,
                                      'font-size',
                                      data['font_size_title_block_new_old'])


def test_dw177(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_NEW_OLD,
                                       'color',
                                       data['font_color_title_block_new_old'])


def test_dw178(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_NEW_OLD,
                                        data['link_image_block_new_old'])


def test_dw179(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_NEW_OLD,
                                       data['title_stub'])


def test_dw180(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PREMIUM, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PREMIUM)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw181(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PREMIUM,
                                 data['title_block_premium'])


def test_dw182(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PREMIUM,
                                 'font-family',
                                 data['font'])


def test_dw183(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PREMIUM,
                                      'font-size',
                                      data['font_size_title_block_premium'])


def test_dw184(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PREMIUM,
                                       'color',
                                       data['font_color_title_block_premium'])


def test_dw185(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PREMIUM,
                                        data['link_image_block_premium'])


def test_dw186(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PREMIUM,
                                       data['title_stub'])


def test_dw187(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_BROKEN, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_BROKEN)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw188(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_BROKEN,
                                 data['title_block_broken'])


def test_dw189(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_BROKEN,
                                 'font-family',
                                 data['font'])


def test_dw190(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_BROKEN,
                                      'font-size',
                                      data['font_size_title_block_broken'])


def test_dw191(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_BROKEN,
                                       'color',
                                       data['font_color_title_block_broken'])


def test_dw192(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_BROKEN,
                                        data['link_image_block_broken'])


def test_dw193(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_BROKEN,
                                       data['title_stub'])


def test_dw194(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_CREDIT, RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_CREDIT)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw195(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_CREDIT,
                                 data['title_block_credit'])


def test_dw196(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_CREDIT,
                                 'font-family',
                                 data['font'])


def test_dw197(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_CREDIT,
                                      'font-size',
                                      data['font_size_title_block_credit'])


def test_dw198(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_CREDIT,
                                       'color',
                                       data['font_color_title_block_credit'])


def test_dw199(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_CREDIT,
                                        data['link_image_block_credit'])


def test_dw200(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_CREDIT,
                                       data['title_stub'])


def test_dw201(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_EMERGENCY,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_EMERGENCY)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw202(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_EMERGENCY,
                                 data['title_block_emergency'])


def test_dw203(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_EMERGENCY,
                                 'font-family',
                                 data['font'])


def test_dw204(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_EMERGENCY,
                                      'font-size',
                                      data['font_size_title_block_emergency'])


def test_dw205(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_EMERGENCY,
                                       'color',
                                       data['font_color_title_block_emergency'])


def test_dw206(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_EMERGENCY,
                                        data['link_image_block_emergency'])


def test_dw207(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_EMERGENCY,
                                       data['title_stub'])


def test_dw208(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_DUPLICATE_PTS,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_DUPLICATE_PTS)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw209(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_DUPLICATE_PTS,
                                 data['title_block_duplicate_pts'])


def test_dw210(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_DUPLICATE_PTS,
                                 'font-family',
                                 data['font'])


def test_dw211(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_DUPLICATE_PTS,
                                      'font-size',
                                      data['font_size_title_block_duplicate_pts'])


def test_dw212(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_DUPLICATE_PTS,
                                       'color',
                                       data['font_color_title_block_duplicate_pts'])


def test_dw213(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_DUPLICATE_PTS,
                                        data['link_image_block_duplicate_pts'])


def test_dw214(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_DUPLICATE_PTS,
                                       data['title_stub'])


def test_dw215(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_ARRESTED,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_ARRESTED)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw216(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_ARRESTED,
                                 data['title_block_arrested'])


def test_dw217(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_ARRESTED,
                                 'font-family',
                                 data['font'])


def test_dw218(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_ARRESTED,
                                      'font-size',
                                      data['font_size_title_block_arrested'])


def test_dw219(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_ARRESTED,
                                       'color',
                                       data['font_color_title_block_arrested'])


def test_dw220(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_ARRESTED,
                                        data['link_image_block_arrested'])


def test_dw221(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_ARRESTED,
                                       data['title_stub'])


def test_dw222(browser):
    contents = (RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PROBLEM,
                RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PROBLEM)
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw223(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_name_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PROBLEM,
                                 data['title_block_problem'])


def test_dw224(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PROBLEM,
                                 'font-family',
                                 data['font'])


def test_dw225(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PROBLEM,
                                      'font-size',
                                      data['font_size_title_block_problem'])


def test_dw226(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomAllPageLocators.LOCATOR_TITLE_BLOCK_PROBLEM,
                                       'color',
                                       data['font_color_title_block_problem'])


def test_dw227(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_image(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PROBLEM,
                                        data['link_image_block_problem'])


def test_dw228(browser):
    test_page = RansomAllPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomAllPageLocators.LOCATOR_TITLE)
    time.sleep(2)
    test_page.checking_validation_stub(RansomAllPageLocators.LOCATOR_IMAGE_BLOCK_PROBLEM,
                                       data['title_stub'])
