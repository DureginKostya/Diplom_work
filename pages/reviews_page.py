import re
import time
from selenium.webdriver import ActionChains
from pages.BaseApp import BasePage


class ReviewsPage(BasePage):

    def checking_background_color_button(self, locator_btn, property_elm, rsl, cursor=0):
        if cursor == 1:
            self.hovering_over_an_element(locator_btn)
        background_color_btn = self.get_element_property(locator_btn, property_elm)
        background_color_btn = background_color_btn[25:76]
        assert background_color_btn == rsl

    def checking_background_color_slider(self, locator_btn, property_elm, rsl):
        background_color_sld = self.get_element_property(locator_btn, property_elm)
        assert background_color_sld == rsl

    def checking_click_btn_back(self, name_user):
        time.sleep(3)
        self.make_screenshot(name_user)
        assert self.get_image_comparison(name_user) < 20

    def checking_contents_page(self, contents):
        key = True
        for element in contents:
            value = self.is_element_present(element)
            if not value:
                key = False
                break
        assert key

    def checking_font_color_text(self, locator, property_elm, rsl):
        font_color_text = self.get_element_property(locator, property_elm)
        assert font_color_text == rsl

    def checking_font_size_text(self, locator, property_elm, rsl):
        font_size_text = self.get_element_property(locator, property_elm)
        assert font_size_text == rsl

    def checking_font_text(self, locator, property_elm, rsl):
        font_text = self.get_element_property(locator, property_elm)[1:9]
        assert font_text == rsl

    def checking_icon(self, locator, name_user):
        self.make_screenshot_icon(locator, name_user)
        assert self.get_image_comparison(name_user) < 20

    def checking_name_text(self, locator, rsl):
        text_user = self.search_element(locator).text
        result = re.sub("\n", ' ', text_user)
        assert result == rsl

    def checking_operation_slider(self, locator_btn_1, locator_btn_2, name_user_1, name_user_2):
        same = []
        button_1 = self.search_element(locator_btn_1)
        button_1.click()
        time.sleep(3)
        self.make_screenshot(name_user_1)
        same.append(self.get_image_comparison(name_user_1) < 20)
        button_2 = self.search_element(locator_btn_2)
        button_2.click()
        time.sleep(3)
        self.make_screenshot(name_user_2)
        same.append(self.get_image_comparison(name_user_2) < 20)
        assert False not in same

    def checking_size_button(self, locator_btn, height_elm, width_el, rsl_height, rsl_width):
        height_size_btn = self.get_element_property(locator_btn, height_elm)
        width_size_btn = self.get_element_property(locator_btn, width_el)
        assert height_size_btn == rsl_height and width_size_btn == rsl_width

    def checking_validation_image(self, locator, rsl):
        img = self.search_element(locator)
        result = img.get_attribute('src')
        assert result == rsl

    def checking_type_cursor(self, locator, property_elm, rsl):
        type_cursor = self.get_element_property(locator, property_elm)
        assert type_cursor == rsl

    def click_button(self, locator_btn, locator_rsl, rsl):
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(2)
        title = self.search_element(locator_rsl).text
        assert title == rsl

    def hovering_over_an_element(self, locator):
        hover = self.search_element(locator)
        ActionChains(self.driver).move_to_element(hover).perform()
