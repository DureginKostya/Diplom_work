import re
import time
from pages.BaseApp import BasePage


class QuestionsAnswersPage(BasePage):

    def checking_background_color_button(self, locator_btn, property_elm, rsl):
        background_color_btn = self.get_element_property(locator_btn, property_elm)
        background_color_btn = background_color_btn[26:78]
        assert background_color_btn == rsl

    def checking_collapse_question(self, locator_btn, locator_answer):
        if self.is_not_element_present(locator_answer):
            self.click_button(locator_btn)
        self.click_button(locator_btn)
        time.sleep(2)
        assert self.is_not_element_present(locator_answer)

    def checking_contents_page(self, contents):
        key = True
        for element in contents:
            value = self.is_element_present(element)
            if not value:
                key = False
                break
        assert key

    def checking_disclosure_of_one_question(self, content, locator_btn1, locator_asw, locator_btn2, rsl):
        examination = []
        self.click_button(locator_btn1)
        time.sleep(1)
        examination.append(self.is_element_present(locator_asw))
        self.click_button(locator_btn2)
        time.sleep(1)
        examination.append(self.is_element_present(rsl))
        examination2 = []
        for answers in content:
            if self.is_element_present(answers):
                examination2.append(answers)
        assert len(examination2) == 1 and examination2[0] == rsl and False not in examination

    def checking_expand_question(self, locator_btn, locator_answer):
        if self.is_element_present(locator_answer):
            self.click_button(locator_btn)
        self.click_button(locator_btn)
        time.sleep(2)
        assert self.is_element_present(locator_answer)

    def checking_font_color_text(self, locator, property_elm, rsl):
        font_color_text = self.get_element_property(locator, property_elm)
        assert font_color_text == rsl

    def checking_font_size_text(self, locator, property_elm, rsl):
        font_size_text = self.get_element_property(locator, property_elm)
        assert font_size_text == rsl

    def checking_font_text(self, locator, property_elm, rsl):
        font_text = self.get_element_property(locator, property_elm)[1:9]
        assert font_text == rsl

    def checking_name_button(self, locator, rsl):
        text_user = self.search_element(locator)
        result = text_user.get_attribute('class')
        assert result == rsl

    def checking_name_text(self, locator, rsl):
        text_user = self.search_element(locator).text
        result = re.sub("\n", ' ', text_user)
        assert result == rsl

    def checking_type_cursor(self, locator, property_elm, rsl):
        type_cursor = self.get_element_property(locator, property_elm)
        assert type_cursor == rsl

    def click_button(self, locator_btn):
        button = self.search_element(locator_btn)
        button.click()
