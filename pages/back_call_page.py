import re
import time
from selenium.webdriver import ActionChains
from pages.BaseApp import BasePage


class BackCallPage(BasePage):

    def checking_background_color_button(self, locator_btn, property_elm, rsl, cursor=0):
        if cursor == 1:
            self.hovering_over_an_element(locator_btn)
        background_color_btn = self.get_element_property(locator_btn, property_elm)
        background_color_btn = background_color_btn[25:76]
        assert background_color_btn == rsl

    def checking_background_color_field(self, locator_fld, property_elm, rsl):
        background_color_fld = self.get_element_property(locator_fld, property_elm)
        assert background_color_fld == rsl

    def checking_contents_page(self, contents):
        key = True
        for element in contents:
            value = self.is_element_present(element)
            if not value:
                key = False
                break
        assert key

    def checking_font_text_field(self, locator_fld, value, property_elm, rsl):
        self.fill_field(locator_fld, value)
        font_fld = self.get_element_property(locator_fld, property_elm)[1:9]
        assert font_fld == rsl

    def checking_font_color_text(self, locator, property_elm, rsl):
        font_color_text = self.get_element_property(locator, property_elm)
        assert font_color_text == rsl

    def checking_font_color_text_field(self, locator_fld, value, property_elm, rsl):
        self.fill_field(locator_fld, value)
        time.sleep(2)
        font_color_fld = self.get_element_property(locator_fld, property_elm)
        assert font_color_fld == rsl

    def checking_font_size_text(self, locator, property_elm, rsl):
        font_size_text = self.get_element_property(locator, property_elm)
        assert font_size_text == rsl

    def checking_font_size_text_field(self, locator_fld, value, property_elm, rsl):
        self.fill_field(locator_fld, value)
        font_size_fld = self.get_element_property(locator_fld, property_elm)
        assert font_size_fld == rsl

    def checking_font_text(self, locator, property_elm, rsl):
        font_text = self.get_element_property(locator, property_elm)[1:9]
        assert font_text == rsl

    def checking_name_text(self, locator, rsl):
        text_user = self.search_element(locator).text
        result = re.sub("\n", ' ', text_user)
        assert result == rsl

    def checking_negative_examination1(self, fields, locator_btn, locator_fld):
        for key, value in fields.items():
            self.fill_field(key, value)
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(5)
        font_color_fld = self.get_element_property(locator_fld, 'color')
        text_user = self.search_element(locator_fld)
        result = text_user.get_attribute('value')
        assert font_color_fld == 'rgba(238, 110, 110, 1)' and result == ''

    def checking_negative_examination2(self, fields, locator_btn, locator_fld, locator_rsl, rsl):
        for key, value in fields.items():
            self.fill_field(key, value)
        time.sleep(2)
        text_user = self.search_element(locator_fld)
        result = text_user.get_attribute('value')
        value = fields[locator_fld]
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(5)
        title_thank_you = self.search_element(locator_rsl).text
        assert title_thank_you == rsl and result == value[:-1]

    def checking_negative_examination3(self, fields, locator_btn, locator_fld):
        for key, value in fields.items():
            self.fill_field(key, value)
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(5)
        font_color_fld = self.get_element_property(locator_fld, 'color')
        text_user = self.search_element(locator_fld)
        result = text_user.get_attribute('value').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        value = fields[locator_fld]
        assert font_color_fld == 'rgba(238, 110, 110, 1)' and result == value

    def checking_negative_examination4(self, fields, locator_btn, locator_fld, locator_rsl, rsl):
        for key, value in fields.items():
            self.fill_field(key, value)
        time.sleep(2)
        text_user = self.search_element(locator_fld)
        result = text_user.get_attribute('value').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        value = fields[locator_fld]
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(5)
        title_thank_you = self.search_element(locator_rsl).text
        assert title_thank_you == rsl and result == value[:-1]

    def checking_negative_examination5(self, fields, locator_btn, locator_fld, locator_rsl, rsl):
        for key, value in fields.items():
            self.fill_field(key, value)
        time.sleep(2)
        text_user = self.search_element(locator_fld)
        result = text_user.get_attribute('value').replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        value = fields[locator_fld]
        value = '+7' + value[1:11]
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(5)
        title_thank_you = self.search_element(locator_rsl).text
        assert title_thank_you == rsl and result == value

    def checking_positive_examination(self, fields, locator_btn, locator_rsl, rsl):
        for key, value in fields.items():
            self.fill_field(key, value)
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(5)
        title_thank_you = self.search_element(locator_rsl).text
        assert title_thank_you == rsl

    def checking_placeholder(self, locator_fld, rsl):
        text_user = self.search_element(locator_fld)
        placeholder = text_user.get_attribute('placeholder')
        assert placeholder == rsl

    def checking_size_button(self, locator_btn, height_elm, width_el, rsl_height, rsl_width):
        height_size_btn = self.get_element_property(locator_btn, height_elm)
        width_size_btn = self.get_element_property(locator_btn, width_el)
        assert height_size_btn == rsl_height and width_size_btn == rsl_width

    def checking_type_cursor(self, locator, property_elm, rsl):
        type_cursor = self.get_element_property(locator, property_elm)
        assert type_cursor == rsl

    def click_button(self, locator_btn, locator_rsl, rsl):
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(2)
        title = self.search_element(locator_rsl).text
        assert title == rsl

    def fill_field(self, locator_fld, value):
        field = self.search_element(locator_fld)
        field.clear()
        field.send_keys(value)

    def hovering_over_an_element(self, locator):
        hover = self.search_element(locator)
        ActionChains(self.driver).move_to_element(hover).perform()

    def open_window_back_call(self, locator_btn):
        button = self.search_element(locator_btn)
        button.click()
