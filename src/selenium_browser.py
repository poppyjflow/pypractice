# Externals.
from selenium import webdriver
import time

# Locals.

# Hard-coded vals for ease-of-use.


class SeleniumBrowser:
    def __init__(self, browser="chrome"):
        self.browser = browser
        if self.browser == "chrome":
            browserService = webdriver.ChromeService(executable_path='/usr/bin/chromedriver')
            browserOptions = webdriver.ChromeOptions()
            # browserOptions.add_argument('--headless')
            browserOptions.add_argument('--no-sandbox')
            browserOptions.add_argument('--disable-dev-shm-usage')
# driver = webdriver.Chrome('/path/to/your_chrome_driver_dir/chromedriver',chrome_options=chrome_options)
            self.driver = webdriver.Chrome(service=browserService, options=browserOptions)
        elif self.browser == "firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "edge":
            self.driver = webdriver.Edge()
        else:
            raise ValueError("Invalid browser specified. Please use 'chrome', 'firefox', or 'edge'.")

    def navigate_to(self, url):
        self.driver.get(url)

    def find_element(self, locator_type, locator):
        if locator_type == "id":
            element = self.driver.find_element_by_id(locator)
        elif locator_type == "xpath":
            element = self.driver.find_element_by_xpath(locator)
        elif locator_type == "css":
            element = self.driver.find_element_by_css_selector(locator)
        else:
            raise ValueError("Invalid locator type specified. Please use 'id', 'xpath', or 'css'.")
        return element

    def click_element(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.click()

    def send_keys(self, locator_type, locator, text):
        element = self.find_element(locator_type, locator)
        element.send_keys(text)

    def clear_input(self, locator_type, locator):
        element = self.find_element(locator_type, locator)
        element.clear()

    def wait(self, seconds):
        time.sleep(seconds)

    def quit(self):
        self.driver.quit()
