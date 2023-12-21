import time
from selenium.webdriver import ActionChains
from pages.BaseApp import BasePage


class HeaderPage(BasePage):

    def checking_background_color_button(self, locator_btn, property_elm, rsl, cursor=0):
        if cursor == 1:
            self.hovering_over_an_element(locator_btn)
        background_color_btn = self.get_element_property(locator_btn, property_elm)
        if cursor == 1:
            background_color_btn = background_color_btn[25:76]
        assert background_color_btn == rsl

    def checking_close_hamburger_menu(self, locator_btn_open, locator_btn_close, rsl):
        open_btn = self.search_element(locator_btn_open)
        open_btn.click()
        close_btn = self.search_element(locator_btn_close)
        time.sleep(2)
        close_btn.click()
        time.sleep(2)
        assert self.is_not_element_present(rsl)

    def checking_contents_page(self, contents):
        key = True
        for element in contents:
            value = self.is_element_present(element)
            if not value:
                key = False
                break
        assert key

    def checking_favicon(self, locator, name_user):
        self.make_screenshot_icon(locator, name_user)
        assert self.get_image_comparison(name_user) < 20

    def checking_font_button(self, locator_btn, property_elm, rsl):
        font_btn = self.get_element_property(locator_btn, property_elm)[1:9]
        assert font_btn == rsl

    def checking_font_color_button(self, locator_btn, property_elm, rsl, cursor=0):
        if cursor == 1:
            self.hovering_over_an_element(locator_btn)
        font_color_btn = self.get_element_property(locator_btn, property_elm)
        assert font_color_btn == rsl

    def checking_font_size_button(self, locator_btn, property_elm, rsl):
        font_size_btn = self.get_element_property(locator_btn, property_elm)
        assert font_size_btn == rsl

    def checking_name_button(self, locator_btn, rsl):
        button = self.search_element(locator_btn)
        assert button.text == rsl

    def checking_not_contents_page(self, contents, locator):
        key = True
        for element in contents:
            value = self.is_not_element_present(element)
            if not value:
                key = False
                break
        assert key and self.is_element_present(locator)

    def checking_size_button(self, locator_btn, height_elm, width_el, rsl_height, rsl_width):
        height_size_btn = self.get_element_property(locator_btn, height_elm)
        width_size_btn = self.get_element_property(locator_btn, width_el)
        assert height_size_btn == rsl_height and width_size_btn == rsl_width

    def checking_title(self, name):
        name_page = self.driver.title
        assert name_page == name

    def checking_type_cursor(self, locator_btn, property_elm, rsl):
        type_cursor = self.get_element_property(locator_btn, property_elm)
        assert type_cursor == rsl

    def click_button(self, locator_btn, locator_rsl, rsl):
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(2)
        title = self.search_element(locator_rsl).text
        assert title == rsl

    def click_button_navigation(self, locator_btn, name_user):
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(2)
        self.make_screenshot(name_user)
        assert self.get_image_comparison(name_user) < 20

    def hovering_over_an_element(self, locator_btn):
        hover = self.search_element(locator_btn)
        ActionChains(self.driver).move_to_element(hover).perform()
