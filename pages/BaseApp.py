import time
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from PIL import Image
import PIL.ImageChops as ich
import os


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def search_element(self, locator):
        try:
            element = self.driver.find_element(*locator)
        except NoSuchElementException:
            return None
        return element

    def get_element_property(self, locator, property_element):
        element = self.search_element(locator)
        return element.value_of_css_property(property_element)

    def open_site(self):
        return self.driver.get(self.base_url)

    def changed_window_size(self, height, width):
        self.driver.set_window_size(height, width)

    def is_not_element_present(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                ES.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return True
        return False

    def is_element_present(self, locator, timeout=2):
        try:
            WebDriverWait(self.driver, timeout).until(
                ES.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False
        return True

    def go_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def make_screenshot(self, name_user):
        self.driver.save_screenshot(f'screenshots_made/{name_user}_made.png')

    def is_checked(self, item_id):
        checked = self.driver.execute_script(
            f"return document.getElementById('{item_id}').checked"
        )
        return checked

    def make_screenshot_icon(self, locator, name_user):
        time.sleep(2)
        feature_element = self.driver.find_element(*locator)
        feature_element.screenshot(f'screenshots_made/{name_user}_made.png')

    def get_image_comparison(self, name_user):
        user_screen = Image.open(f'screenshots_user/{name_user}_user.png')
        made_screen = Image.open(f'screenshots_made/{name_user}_made.png')
        ich.screen(image1=user_screen, image2=made_screen).save(f'result_screen/{name_user}_rsl_diff.png')
        ich.screen(image1=user_screen, image2=user_screen).save(f'result_screen/{name_user}_rsl_same.png')
        size_diff = os.path.getsize(f'result_screen/{name_user}_rsl_diff.png')
        size_same = os.path.getsize(f'result_screen/{name_user}_rsl_same.png')
        return abs(size_diff - size_same)

    def get_after(self, locator, property_elm):
        element_style = self.driver.execute_script(f'elm = getComputedStyle(document.querySelector("{locator}"),'
                                                   f'"::after"); return elm.getPropertyValue("{property_elm}")')
        return element_style
