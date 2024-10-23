from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearchAutomation:
    def __init__(self):
        # Initialize the webdriver object (no driver path needed)
        self.driver = webdriver.Chrome()

    def launch_browser(self):
        # Launch the Google website
        self.driver.get("https://www.google.com")

    def search_keyword(self, keyword):
        # Find the search input field, input the keyword, and press Enter
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

    def close_browser(self):
        # Wait for a few seconds and close the browser
        time.sleep(5)
        self.driver.quit()

# Create an object of GoogleSearchAutomation class
if __name__ == "__main__":
    google_search = GoogleSearchAutomation()

    # Using the object to perform actions
    google_search.launch_browser()
    google_search.search_keyword("Selenium WebDriver")
    google_search.close_browser()

