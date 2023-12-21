import time
from pages.questions_answers_page import QuestionsAnswersPage
from pages.locators import QuestionsAnswersPageLocators
import yaml

with open('data/testdata_questions_answers.yaml', encoding='utf-8') as file:
    data = yaml.safe_load(file)


def test_dw501(browser):
    contents = (QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS,
                QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_1,
                QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1,
                QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_2,
                QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2,
                QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_3,
                QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3,
                QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_4,
                QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4,
                QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_5,
                QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5,
                QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_6,
                QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6,
                QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_7,
                QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7)
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_contents_page(contents)


def test_dw502(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS,
                                 data['title_questions_answers'])


def test_dw503(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS,
                                 'font-family',
                                 data['font'])


def test_dw504(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS,
                                      'font-size',
                                      data['font_size_title_questions_answers'])


def test_dw505(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS,
                                       'color',
                                       data['font_color_title_questions_answers'])


def test_dw506(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_1,
                                 data['title_question_1'])


def test_dw507(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_1,
                                 'font-family',
                                 data['font'])


def test_dw508(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_1,
                                      'font-size',
                                      data['font_size_title_question_1'])


def test_dw509(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_1,
                                       'color',
                                       data['font_color_title_question_1'])


def test_dw510(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_1,
                                 data['title_answer_1'])


def test_dw511(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_1,
                                 'font-family',
                                 data['font'])


def test_dw512(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_1,
                                      'font-size',
                                      data['font_size_title_answer_1'])


def test_dw513(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_1,
                                       'color',
                                       data['font_color_title_answer_1'])


def test_dw514(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1_EXPAND,
                                   data['title_button_expand'])


def test_dw515(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_background_color_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1,
                                               'background-image',
                                               data['background_color_button'])


def test_dw516(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1_COLLAPSE,
                                   data['title_button_collapse'])


def test_dw517(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_expand_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1,
                                       QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_1)


def test_dw518(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_collapse_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1,
                                         QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_1)


def test_dw519(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_2,
                                 data['title_question_2'])


def test_dw520(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_2,
                                 'font-family',
                                 data['font'])


def test_dw521(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_2,
                                      'font-size',
                                      data['font_size_title_question_2'])


def test_dw522(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_2,
                                       'color',
                                       data['font_color_title_question_2'])


def test_dw523(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_2,
                                 data['title_answer_2'])


def test_dw524(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_2,
                                 'font-family',
                                 data['font'])


def test_dw525(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_2,
                                      'font-size',
                                      data['font_size_title_answer_2'])


def test_dw526(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_2,
                                       'color',
                                       data['font_color_title_answer_2'])


def test_dw527(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2_EXPAND,
                                   data['title_button_expand'])


def test_dw528(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_background_color_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2,
                                               'background-image',
                                               data['background_color_button'])


def test_dw529(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2_COLLAPSE,
                                   data['title_button_collapse'])


def test_dw530(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_expand_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2,
                                       QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_2)


def test_dw531(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_collapse_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2,
                                         QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_2)


def test_dw532(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_3,
                                 data['title_question_3'])


def test_dw533(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_3,
                                 'font-family',
                                 data['font'])


def test_dw534(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_3,
                                      'font-size',
                                      data['font_size_title_question_3'])


def test_dw535(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_3,
                                       'color',
                                       data['font_color_title_question_3'])


def test_dw536(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3,
                                 data['title_answer_3'])


def test_dw537(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3,
                                 'font-family',
                                 data['font'])


def test_dw538(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3,
                                      'font-size',
                                      data['font_size_title_answer_3'])


def test_dw539(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3,
                                       'color',
                                       data['font_color_title_answer_3'])


def test_dw540(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3_EXPAND,
                                   data['title_button_expand'])


def test_dw541(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_background_color_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3,
                                               'background-image',
                                               data['background_color_button'])


def test_dw542(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3_COLLAPSE,
                                   data['title_button_collapse'])


def test_dw543(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_expand_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3,
                                       QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3)


def test_dw544(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_collapse_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3,
                                         QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3)


def test_dw545(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_4,
                                 data['title_question_4'])


def test_dw546(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_4,
                                 'font-family',
                                 data['font'])


def test_dw547(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_4,
                                      'font-size',
                                      data['font_size_title_question_4'])


def test_dw548(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_4,
                                       'color',
                                       data['font_color_title_question_4'])


def test_dw549(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_4,
                                 data['title_answer_4'])


def test_dw550(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_4,
                                 'font-family',
                                 data['font'])


def test_dw551(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_4,
                                      'font-size',
                                      data['font_size_title_answer_4'])


def test_dw552(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_4,
                                       'color',
                                       data['font_color_title_answer_4'])


def test_dw553(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4_EXPAND,
                                   data['title_button_expand'])


def test_dw554(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_background_color_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4,
                                               'background-image',
                                               data['background_color_button'])


def test_dw555(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4_COLLAPSE,
                                   data['title_button_collapse'])


def test_dw556(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_expand_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4,
                                       QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_4)


def test_dw557(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_collapse_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4,
                                         QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_4)


def test_dw558(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_5,
                                 data['title_question_5'])


def test_dw559(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_5,
                                 'font-family',
                                 data['font'])


def test_dw560(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_5,
                                      'font-size',
                                      data['font_size_title_question_5'])


def test_dw561(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_5,
                                       'color',
                                       data['font_color_title_question_5'])


def test_dw562(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_5,
                                 data['title_answer_5'])


def test_dw563(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_5,
                                 'font-family',
                                 data['font'])


def test_dw564(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_5,
                                      'font-size',
                                      data['font_size_title_answer_5'])


def test_dw565(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_5,
                                       'color',
                                       data['font_color_title_answer_5'])


def test_dw566(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5_EXPAND,
                                   data['title_button_expand'])


def test_dw567(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_background_color_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5,
                                               'background-image',
                                               data['background_color_button'])


def test_dw568(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5_COLLAPSE,
                                   data['title_button_collapse'])


def test_dw569(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_expand_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5,
                                       QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_5)


def test_dw570(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_collapse_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5,
                                         QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_5)


def test_dw571(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_6,
                                 data['title_question_6'])


def test_dw572(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_6,
                                 'font-family',
                                 data['font'])


def test_dw573(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_6,
                                      'font-size',
                                      data['font_size_title_question_6'])


def test_dw574(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_6,
                                       'color',
                                       data['font_color_title_question_6'])


def test_dw575(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6,
                                 data['title_answer_6'])


def test_dw576(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6,
                                 'font-family',
                                 data['font'])


def test_dw577(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6,
                                      'font-size',
                                      data['font_size_title_answer_6'])


def test_dw578(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6,
                                       'color',
                                       data['font_color_title_answer_6'])


def test_dw579(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6_EXPAND,
                                   data['title_button_expand'])


def test_dw580(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_background_color_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6,
                                               'background-image',
                                               data['background_color_button'])


def test_dw581(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6_COLLAPSE,
                                   data['title_button_collapse'])


def test_dw582(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_expand_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6,
                                       QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6)


def test_dw583(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_collapse_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6,
                                         QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6)


def test_dw584(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_7,
                                 data['title_question_7'])


def test_dw585(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_7,
                                 'font-family',
                                 data['font'])


def test_dw586(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_7,
                                      'font-size',
                                      data['font_size_title_question_7'])


def test_dw587(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTION_7,
                                       'color',
                                       data['font_color_title_question_7'])


def test_dw588(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7)
    time.sleep(2)
    test_page.checking_name_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_7,
                                 data['title_answer_7'])


def test_dw589(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7)
    time.sleep(2)
    test_page.checking_font_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_7,
                                 'font-family',
                                 data['font'])


def test_dw590(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7)
    time.sleep(2)
    test_page.checking_font_size_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_7,
                                      'font-size',
                                      data['font_size_title_answer_7'])


def test_dw591(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    test_page.click_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7)
    time.sleep(2)
    test_page.checking_font_color_text(QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_7,
                                       'color',
                                       data['font_color_title_answer_7'])


def test_dw592(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7_EXPAND,
                                   data['title_button_expand'])


def test_dw593(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_background_color_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7,
                                               'background-image',
                                               data['background_color_button'])


def test_dw594(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_name_button(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7_COLLAPSE,
                                   data['title_button_collapse'])


def test_dw595(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_expand_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7,
                                       QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_7)


def test_dw596(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_collapse_question(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7,
                                         QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_7)


def test_dw597(browser):
    content = [QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_1, QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_2,
               QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3, QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3,
               QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_5, QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6,
               QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_7]
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_disclosure_of_one_question(content,
                                                  QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3,
                                                  QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_3,
                                                  QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6,
                                                  QuestionsAnswersPageLocators.LOCATOR_TITLE_ANSWER_6, )


def test_dw598(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_type_cursor(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_1,
                                   'cursor',
                                   data['type_cursor_button'])


def test_dw599(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_type_cursor(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_2,
                                   'cursor',
                                   data['type_cursor_button'])


def test_dw600(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_type_cursor(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_3,
                                   'cursor',
                                   data['type_cursor_button'])


def test_dw601(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_type_cursor(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_4,
                                   'cursor',
                                   data['type_cursor_button'])


def test_dw602(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_type_cursor(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_5,
                                   'cursor',
                                   data['type_cursor_button'])


def test_dw603(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_type_cursor(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_6,
                                   'cursor',
                                   data['type_cursor_button'])


def test_dw604(browser):
    test_page = QuestionsAnswersPage(browser, data['url'])
    test_page.open_site()
    test_page.go_to_element(QuestionsAnswersPageLocators.LOCATOR_TITLE_QUESTIONS_ANSWERS)
    time.sleep(2)
    test_page.checking_type_cursor(QuestionsAnswersPageLocators.LOCATOR_BUTTON_QUESTION_7,
                                   'cursor',
                                   data['type_cursor_button'])
