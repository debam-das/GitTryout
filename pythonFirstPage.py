from locators import locators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class searchPage:
    def __init__(self, driver):
        self.driver = driver
        self.locator_searchBox_name = locators.serachBox_name

    def firstMethod(self, keyword_to_search):
        pilot = self.driver
        assert "Python" in pilot.title
        elem = pilot.find_element_by_name(self.locator_searchBox_name)
        elem.clear()
        elem.send_keys(keyword_to_search)
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in pilot.page_source
