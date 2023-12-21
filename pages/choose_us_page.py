import re
from pages.BaseApp import BasePage


class ChooseUsPage(BasePage):

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
