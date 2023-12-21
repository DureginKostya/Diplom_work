import time
from pages.reviews_page import ReviewsPage
from pages.locators import ReviewsPageLocators
import yaml


with open('data/testdata_reviews.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw605(browser):
    contents = (ReviewsPageLocators.LOCATOR_TITLE_REVIEWS, ReviewsPageLocators.LOCATOR_BUTTON_BACK,
                ReviewsPageLocators.LOCATOR_BUTTON_FORWARD, ReviewsPageLocators.LOCATOR_BLOCK_REVIEW_1,
                ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1, ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_2,
                ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_3, ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_4,
                ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_5, ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_6,
                ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_7)
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw606(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS,
                                 data['title_reviews'])


def test_dw607(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS,
                                 'font-family',
                                 data['font'])


def test_dw608(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS,
                                      'font-size',
                                      data['font_size_title_ransom_all'])


def test_dw609(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS,
                                       'color',
                                       data['font_color_title_ransom_all'])


def test_dw610(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_icon(ReviewsPageLocators.LOCATOR_BUTTON_BACK,
                            data['title_icon_btn_back'])


def test_dw612(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_background_color_button(ReviewsPageLocators.LOCATOR_BUTTON_BACK,
                                               'background-image',
                                               data['background_color_btn_back_not_cursor'])


def test_dw613(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_background_color_button(ReviewsPageLocators.LOCATOR_BUTTON_BACK,
                                               'background-image',
                                               data['background_color_btn_back_with_cursor'],
                                               1)


def test_dw614(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_size_button(ReviewsPageLocators.LOCATOR_BUTTON_BACK,
                                   'height',
                                   'width',
                                   data['height_btn_back'],
                                   data['width_btn_back'])


def test_dw617(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    button = test_page.search_element(ReviewsPageLocators.LOCATOR_BUTTON_BACK)
    button.click()
    time.sleep(2)
    test_page.checking_click_btn_back(data['img_btn_back_review'])


def test_dw618(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_icon(ReviewsPageLocators.LOCATOR_BUTTON_FORWARD,
                            data['title_icon_btn_forward'])


def test_dw620(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_background_color_button(ReviewsPageLocators.LOCATOR_BUTTON_FORWARD,
                                               'background-image',
                                               data['background_color_btn_forward_not_cursor'])


def test_dw621(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_background_color_button(ReviewsPageLocators.LOCATOR_BUTTON_FORWARD,
                                               'background-image',
                                               data['background_color_btn_forward_with_cursor'],
                                               1)


def test_dw622(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_size_button(ReviewsPageLocators.LOCATOR_BUTTON_FORWARD,
                                   'height',
                                   'width',
                                   data['height_btn_forward'],
                                   data['width_btn_forward'])


def test_dw623(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    button = test_page.search_element(ReviewsPageLocators.LOCATOR_BUTTON_FORWARD)
    button.click()
    time.sleep(2)
    test_page.checking_click_btn_back(data['img_btn_forward_review'])


def test_dw625(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_size_button(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1,
                                   'height',
                                   'width',
                                   data['height_slider_btn'],
                                   data['width_slider_btn'])


def test_dw626(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    slider = test_page.search_element(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1)
    slider.click()
    time.sleep(2)
    test_page.checking_background_color_slider(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1,
                                               'background-color',
                                               data['slider_1_color'])


def test_dw627(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    slider = test_page.search_element(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1)
    slider.click()
    time.sleep(2)
    test_page.checking_background_color_slider(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_2,
                                               'background-color',
                                               data['slider_2_color'])


def test_dw628(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    slider = test_page.search_element(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1)
    slider.click()
    time.sleep(2)
    test_page.checking_background_color_slider(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_3,
                                               'background-color',
                                               data['slider_3_color'])


def test_dw629(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    slider = test_page.search_element(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1)
    slider.click()
    time.sleep(2)
    test_page.checking_background_color_slider(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_4,
                                               'background-color',
                                               data['slider_4_color'])


def test_dw630(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    slider = test_page.search_element(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1)
    slider.click()
    time.sleep(2)
    test_page.checking_background_color_slider(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_5,
                                               'background-color',
                                               data['slider_5_color'])


def test_dw631(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_operation_slider(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_4,
                                        ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_2, data['img_slider_4_review'],
                                        data['img_slider_2_review'])


def test_dw632(browser):
    contents = (ReviewsPageLocators.LOCATOR_TITLE_BLOCK_REVIEW_1, ReviewsPageLocators.LOCATOR_TEXT_REVIEW_1,
                ReviewsPageLocators.LOCATOR_BUTTON_EXPAND_REVIEW_1, ReviewsPageLocators.LOCATOR_IMAGE_REVIEW_1,
                ReviewsPageLocators.LOCATOR_ICON_PRICE_1, ReviewsPageLocators.LOCATOR_TITLE_PRICE_KARTEKA_1,
                ReviewsPageLocators.LOCATOR_PRICE_KARTEKA_1, ReviewsPageLocators.LOCATOR_TITLE_PRICE_OTHER_1,
                ReviewsPageLocators.LOCATOR_PRICE_OTHER_1)
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw633(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_TITLE_BLOCK_REVIEW_1,
                                 data['title_block_review_1'])


def test_dw634(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_TITLE_BLOCK_REVIEW_1,
                                 'font-family',
                                 data['font'])


def test_dw635(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_TITLE_BLOCK_REVIEW_1,
                                      'font-size',
                                      data['font_size_title_block_review_1'])


def test_dw636(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_TITLE_BLOCK_REVIEW_1,
                                       'color',
                                       data['font_color_title_block_review_1'])


def test_dw637(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_TEXT_REVIEW_1,
                                 data['text_review_1'])


def test_dw638(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_TEXT_REVIEW_1,
                                 'font-family',
                                 data['font'])


def test_dw639(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_TEXT_REVIEW_1,
                                      'font-size',
                                      data['font_size_text_review_1'])


def test_dw640(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_TEXT_REVIEW_1,
                                       'color',
                                       data['font_color_text_review_1'])


def test_dw641(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_BUTTON_EXPAND_REVIEW_1,
                                 data['title_btn_expand_review_1'])


def test_dw642(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_BUTTON_EXPAND_REVIEW_1,
                                 'font-family',
                                 data['font'])


def test_dw643(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_BUTTON_EXPAND_REVIEW_1,
                                      'font-size',
                                      data['font_size_title_btn_expand_review_1'])


def test_dw644(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_BUTTON_EXPAND_REVIEW_1,
                                       'color',
                                       data['font_color_title_btn_expand_review_1'])


def test_dw645(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.click_button(ReviewsPageLocators.LOCATOR_BUTTON_EXPAND_REVIEW_1,
                           ReviewsPageLocators.LOCATOR_TITLE_FULL_REVIEW_1, data['title_full_review_1'])


def test_dw646(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_validation_image(ReviewsPageLocators.LOCATOR_IMAGE_REVIEW_1,
                                        data['link_image_review_1'])


def test_dw647(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_icon(ReviewsPageLocators.LOCATOR_ICON_PRICE_1,
                            data['title_icon_price'])


def test_dw648(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_KARTEKA_1,
                                 data['title_price_karteka_1'])


def test_dw649(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_KARTEKA_1,
                                 'font-family',
                                 data['font'])


def test_dw650(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_KARTEKA_1,
                                      'font-size',
                                      data['font_size_title_price_karteka_1'])


def test_dw651(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_KARTEKA_1,
                                       'color',
                                       data['font_color_title_price_karteka_1'])


def test_dw652(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_PRICE_KARTEKA_1,
                                 data['price_karteka_1'])


def test_dw653(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_PRICE_KARTEKA_1,
                                 'font-family',
                                 data['font'])


def test_dw654(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_PRICE_KARTEKA_1,
                                      'font-size',
                                      data['font_size_price_karteka_1'])


def test_dw655(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_PRICE_KARTEKA_1,
                                       'color',
                                       data['font_color_price_karteka_1'])


def test_dw656(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_OTHER_1,
                                 data['title_price_other_1'])


def test_dw657(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_OTHER_1,
                                 'font-family',
                                 data['font'])


def test_dw658(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_OTHER_1,
                                      'font-size',
                                      data['font_size_title_price_other_1'])


def test_dw659(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_TITLE_PRICE_OTHER_1,
                                       'color',
                                       data['font_color_title_price_other_1'])


def test_dw660(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_name_text(ReviewsPageLocators.LOCATOR_PRICE_OTHER_1,
                                 data['price_other_1'])


def test_dw661(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_text(ReviewsPageLocators.LOCATOR_PRICE_OTHER_1,
                                 'font-family',
                                 data['font'])


def test_dw662(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_size_text(ReviewsPageLocators.LOCATOR_PRICE_OTHER_1,
                                      'font-size',
                                      data['font_size_price_other_1'])


def test_dw663(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_font_color_text(ReviewsPageLocators.LOCATOR_PRICE_OTHER_1,
                                       'color',
                                       data['font_color_price_other_1'])


def test_dw664(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_BACK,
                                   'cursor',
                                   data['type_cursor_btn_back'])


def test_dw665(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_FORWARD,
                                   'cursor',
                                   data['type_cursor_btn_forward'])


def test_dw666(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_EXPAND_REVIEW_1,
                                   'cursor',
                                   data['type_cursor_btn_expand_review'])


def test_dw667(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_1,
                                   'cursor',
                                   data['type_cursor_slider'])


def test_dw668(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_2,
                                   'cursor',
                                   data['type_cursor_slider'])


def test_dw669(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_3,
                                   'cursor',
                                   data['type_cursor_slider'])


def test_dw670(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_4,
                                   'cursor',
                                   data['type_cursor_slider'])


def test_dw671(browser):
    test_page = ReviewsPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(ReviewsPageLocators.LOCATOR_TITLE_REVIEWS)
    time.sleep(2)
    test_page.checking_type_cursor(ReviewsPageLocators.LOCATOR_BUTTON_SLIDER_5,
                                   'cursor',
                                   data['type_cursor_slider'])
