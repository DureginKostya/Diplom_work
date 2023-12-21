import time
from pages.ransom_page import RansomPage
from pages.locators import RansomPageLocators
import yaml


with open('data/testdata_ransom.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw439(browser):
    contents = (RansomPageLocators.LOCATOR_TITLE_PAGE, RansomPageLocators.LOCATOR_TITLE_APPLICATION_EVALUATION,
                RansomPageLocators.LOCATOR_TITLE_DEPARTURE_INSPECTION,
                RansomPageLocators.LOCATOR_TITLE_REGISTRATION_REDEMPTION,
                RansomPageLocators.LOCATOR_TITLE_CASH_BACK)
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw440(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_TITLE_PAGE,
                                 data['title_ransom'])


def test_dw441(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_TITLE_PAGE,
                                 'font-family',
                                 data['font'])


def test_dw442(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_TITLE_PAGE,
                                      'font-size',
                                      data['font_size_title_ransom'])


def test_dw443(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_TITLE_PAGE,
                                       'color',
                                       data['font_color_title_ransom'])


def test_dw444(browser):
    contents = (RansomPageLocators.LOCATOR_TITLE_APPLICATION_EVALUATION,
                RansomPageLocators.LOCATOR_DESCRIPTION_APPLICATION_EVALUATION,
                RansomPageLocators.LOCATOR_ICON_APPLICATION_EVALUATION)
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw445(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_TITLE_APPLICATION_EVALUATION,
                                 data['title_application_evaluation_ransom'])


def test_dw446(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_TITLE_APPLICATION_EVALUATION,
                                 'font-family',
                                 data['font'])


def test_dw447(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_TITLE_APPLICATION_EVALUATION,
                                      'font-size',
                                      data['font_size_title_application_evaluation_ransom'])


def test_dw448(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_TITLE_APPLICATION_EVALUATION,
                                       'color',
                                       data['font_color_title_application_evaluation_ransom'])


def test_dw449(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_1,
                                        'content',
                                        data['title_number_step_1_ransom'])


def test_dw450(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_1,
                                             'font-family',
                                             data['font'])


def test_dw451(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_1,
                                                  'font-size',
                                                  data['font_size_title_number_step_1_ransom'])


def test_dw452(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_1,
                                                   'color',
                                                   data['font_color_title_number_step_1_ransom'])


def test_dw453(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_DESCRIPTION_APPLICATION_EVALUATION,
                                 data['description_application_evaluation_ransom'])


def test_dw454(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_DESCRIPTION_APPLICATION_EVALUATION,
                                 'font-family',
                                 data['font'])


def test_dw455(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_DESCRIPTION_APPLICATION_EVALUATION,
                                      'font-size',
                                      data['font_size_description_application_evaluation_ransom'])


def test_dw456(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_DESCRIPTION_APPLICATION_EVALUATION,
                                       'color',
                                       data['font_color_description_application_evaluation_ransom'])


def test_dw458(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(RansomPageLocators.LOCATOR_ICON_APPLICATION_EVALUATION,
                            data['title_icon_application_evaluation'])


def test_dw459(browser):
    contents = (RansomPageLocators.LOCATOR_TITLE_DEPARTURE_INSPECTION,
                RansomPageLocators.LOCATOR_DESCRIPTION_DEPARTURE_INSPECTION,
                RansomPageLocators.LOCATOR_ICON_DEPARTURE_INSPECTION)
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw460(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_TITLE_DEPARTURE_INSPECTION,
                                 data['title_departure_inspection_ransom'])


def test_dw461(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_TITLE_DEPARTURE_INSPECTION,
                                 'font-family',
                                 data['font'])


def test_dw462(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_TITLE_DEPARTURE_INSPECTION,
                                      'font-size',
                                      data['font_size_title_departure_inspection_ransom'])


def test_dw463(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_TITLE_DEPARTURE_INSPECTION,
                                       'color',
                                       data['font_color_title_departure_inspection_ransom'])


def test_dw464(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_2,
                                        'content',
                                        data['title_number_step_2_ransom'])


def test_dw465(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_2,
                                             'font-family',
                                             data['font'])


def test_dw466(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_2,
                                                  'font-size',
                                                  data['font_size_title_number_step_2_ransom'])


def test_dw467(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_2,
                                                   'color',
                                                   data['font_color_title_number_step_2_ransom'])


def test_dw468(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_DESCRIPTION_DEPARTURE_INSPECTION,
                                 data['description_departure_inspection_ransom'])


def test_dw469(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_DESCRIPTION_DEPARTURE_INSPECTION,
                                 'font-family',
                                 data['font'])


def test_dw470(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_DESCRIPTION_DEPARTURE_INSPECTION,
                                      'font-size',
                                      data['font_size_description_departure_inspection_ransom'])


def test_dw471(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_DESCRIPTION_DEPARTURE_INSPECTION,
                                       'color',
                                       data['font_color_description_departure_inspection_ransom'])


def test_dw472(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(RansomPageLocators.LOCATOR_ICON_DEPARTURE_INSPECTION,
                            data['title_icon_departure_inspection'])


def test_dw473(browser):
    contents = (RansomPageLocators.LOCATOR_TITLE_REGISTRATION_REDEMPTION,
                RansomPageLocators.LOCATOR_DESCRIPTION_REGISTRATION_REDEMPTION,
                RansomPageLocators.LOCATOR_ICON_REGISTRATION_REDEMPTION)
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw474(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_TITLE_REGISTRATION_REDEMPTION,
                                 data['title_registration_redemption_ransom'])


def test_dw475(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_TITLE_REGISTRATION_REDEMPTION,
                                 'font-family',
                                 data['font'])


def test_dw476(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_TITLE_REGISTRATION_REDEMPTION,
                                      'font-size',
                                      data['font_size_title_registration_redemption_ransom'])


def test_dw477(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_TITLE_REGISTRATION_REDEMPTION,
                                       'color',
                                       data['font_color_title_registration_redemption_ransom'])


def test_dw478(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_3,
                                        'content',
                                        data['title_number_step_3_ransom'])


def test_dw479(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_3,
                                             'font-family',
                                             data['font'])


def test_dw480(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_3,
                                                  'font-size',
                                                  data['font_size_title_number_step_3_ransom'])


def test_dw481(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_3,
                                                   'color',
                                                   data['font_color_title_number_step_3_ransom'])


def test_dw482(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_DESCRIPTION_REGISTRATION_REDEMPTION,
                                 data['description_registration_redemption_ransom'])


def test_dw483(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_DESCRIPTION_REGISTRATION_REDEMPTION,
                                 'font-family',
                                 data['font'])


def test_dw484(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_DESCRIPTION_REGISTRATION_REDEMPTION,
                                      'font-size',
                                      data['font_size_description_registration_redemption_ransom'])


def test_dw485(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_DESCRIPTION_REGISTRATION_REDEMPTION,
                                       'color',
                                       data['font_color_description_registration_redemption_ransom'])


def test_dw486(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(RansomPageLocators.LOCATOR_ICON_REGISTRATION_REDEMPTION,
                            data['title_icon_registration_redemption'])


def test_dw487(browser):
    contents = (RansomPageLocators.LOCATOR_TITLE_CASH_BACK,
                RansomPageLocators.LOCATOR_DESCRIPTION_CASH_BACK,
                RansomPageLocators.LOCATOR_ICON_CASH_BACK)
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw488(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_TITLE_CASH_BACK,
                                 data['title_cash_back_ransom'])


def test_dw489(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_TITLE_CASH_BACK,
                                 'font-family',
                                 data['font'])


def test_dw490(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_TITLE_CASH_BACK,
                                      'font-size',
                                      data['font_size_title_cash_back_ransom'])


def test_dw491(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_TITLE_CASH_BACK,
                                       'color',
                                       data['font_color_title_cash_back_ransom'])


def test_dw492(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_4,
                                        'content',
                                        data['title_number_step_4_ransom'])


def test_dw493(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_4,
                                             'font-family',
                                             data['font'])


def test_dw494(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_4,
                                                  'font-size',
                                                  data['font_size_title_number_step_4_ransom'])


def test_dw495(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text_number_step(RansomPageLocators.LOCATOR_NUMBER_STEP_4,
                                                   'color',
                                                   data['font_color_title_number_step_4_ransom'])


def test_dw496(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_name_text(RansomPageLocators.LOCATOR_DESCRIPTION_CASH_BACK,
                                 data['description_cash_back_ransom'])


def test_dw497(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_text(RansomPageLocators.LOCATOR_DESCRIPTION_CASH_BACK,
                                 'font-family',
                                 data['font'])


def test_dw498(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_size_text(RansomPageLocators.LOCATOR_DESCRIPTION_CASH_BACK,
                                      'font-size',
                                      data['font_size_description_cash_back_ransom'])


def test_dw499(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(RansomPageLocators.LOCATOR_TITLE_PAGE)
    time.sleep(2)
    test_page.checking_font_color_text(RansomPageLocators.LOCATOR_DESCRIPTION_CASH_BACK,
                                       'color',
                                       data['font_color_description_cash_back_ransom'])


def test_dw500(browser):
    test_page = RansomPage(browser, data['url'])
    test_page.open_site()
    test_page.checking_icon(RansomPageLocators.LOCATOR_ICON_CASH_BACK,
                            data['title_icon_cash_back'])
