import os
import time
from selenium.webdriver import ActionChains
from pages.BaseApp import BasePage
from PIL import Image
import PIL.ImageChops as ich


class HamburgerMenuPage(BasePage):

    def checking_background_color_button(self, locator_btn_open, locator_btn, property_elm, rsl, cursor=0):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        if cursor == 1:
            self.hovering_over_an_element(locator_btn)
        background_color_btn = self.get_element_property(locator_btn, property_elm)
        if cursor == 1:
            background_color_btn = background_color_btn[25:76]
        assert background_color_btn == rsl

    def checking_contents_page(self, contents, locator_btn):
        self.open_hamburger_menu(locator_btn)
        key = True
        for element in contents:
            value = self.is_element_present(element)
            if not value:
                key = False
                break
        assert key

    def checking_font_button(self, locator_btn_open, locator_btn, property_elm, rsl):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        font_btn = self.get_element_property(locator_btn, property_elm)[1:9]
        assert font_btn == rsl

    def checking_font_color_button(self, locator_btn_open, locator_btn, property_elm, rsl, cursor=0):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        if cursor == 1:
            self.hovering_over_an_element(locator_btn)
        font_color_btn = self.get_element_property(locator_btn, property_elm)
        assert font_color_btn == rsl

    def checking_font_size_button(self, locator_btn_open, locator_btn, property_elm, rsl):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        font_size_btn = self.get_element_property(locator_btn, property_elm)
        assert font_size_btn == rsl

    def checking_name_button(self, locator_btn_open, locator_btn, rsl):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        button = self.search_element(locator_btn)
        assert button.text == rsl

    def checking_size_button(self, locator_btn_open, locator_btn, height_elm, width_el, rsl_height, rsl_width):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        height_size_btn = self.get_element_property(locator_btn, height_elm)
        width_size_btn = self.get_element_property(locator_btn, width_el)
        assert height_size_btn == rsl_height and width_size_btn == rsl_width

    def checking_type_cursor(self, locator_btn_open, locator_btn, property_elm, rsl):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        type_cursor = self.get_element_property(locator_btn, property_elm)
        assert type_cursor == rsl

    def click_button(self, locator_btn_open, locator_btn, locator_rsl, rsl):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(2)
        title = self.search_element(locator_rsl).text
        assert title == rsl

    def click_button_navigation(self, locator_btn_open, locator_btn, name_user):
        self.open_hamburger_menu(locator_btn_open)
        time.sleep(2)
        button = self.search_element(locator_btn)
        button.click()
        time.sleep(2)
        self.make_screenshot(name_user)
        user_screen = Image.open(f'screenshots_user/{name_user}_user_1280.png')
        made_screen = Image.open(f'screenshots_made/{name_user}_made.png')
        ich.screen(image1=user_screen, image2=made_screen).save(f'result_screen/{name_user}_rsl_diff.png')
        ich.screen(image1=user_screen, image2=user_screen).save(f'result_screen/{name_user}_rsl_same.png')
        size_diff = os.path.getsize(f'result_screen/{name_user}_rsl_diff.png')
        size_same = os.path.getsize(f'result_screen/{name_user}_rsl_same.png')
        assert abs(size_same - size_diff) < 20

    def hovering_over_an_element(self, locator_btn):
        hover = self.search_element(locator_btn)
        ActionChains(self.driver).move_to_element(hover).perform()

    def open_hamburger_menu(self, locator_btn):
        button = self.search_element(locator_btn)
        button.click()
