import unittest
from webdriver import Driver
from values import strings

from pageobjects.homescreen import HomeScreen


class TestQABoy(unittest.TestCase):

    # Method will run before each of our test cases
    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)

    # The method name will begin with 'test_'
    # because pytest needs this naming convention to identify al the test cases in our class.
    def test_home_screen_components(self):
        home_screen = HomeScreen(self.driver)
        home_screen.validate_title_is_present()
        home_screen.validate_icon_is_present()
        home_screen.validate_menu_options_are_present()
        home_screen.validate_posts_are_visible()
        home_screen.validate_social_media_links()

    # Method will run after each of our test cases
    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
