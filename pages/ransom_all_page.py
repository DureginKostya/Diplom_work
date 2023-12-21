import re
from pages.BaseApp import BasePage


class RansomAllPage(BasePage):

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

    def checking_name_text(self, locator, rsl):
        text_user = self.search_element(locator).text
        result = re.sub("\n", ' ', text_user)
        assert result == rsl

    def checking_validation_image(self, locator, rsl):
        img = self.search_element(locator)
        result = img.get_attribute('src')
        assert result == rsl

    def checking_validation_stub(self, locator, rsl):
        stub = self.search_element(locator)
        result = stub.get_attribute('alt')
        assert result == rsl
