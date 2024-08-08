from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class WebDriver:

    # No modificar
    def __init__(self):
        self.active_tab = 0
        self.driver = None
        self.tabs = []

    def initialize_driver(self) -> None:
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)


    def load_page(self, page: str) -> None:
        self.driver.get(page)


    def new_tab(self, page: str) -> None:
        self.driver.execute_script(f"window.open('{page}')")
        self.tabs.append(page)
        self.active_tab = len(self.tabs) - 1


    def change_tab(self, page_index: int) -> None: 
        if page_index < len(self.tabs):
            self.driver.switch_to.window(self.tabs[page_index])
            self.active_tab = page_index


    def close_tab(self) -> None:
        self.driver.close()
        del self.tabs[self.active_tab]
        if self.active_tab >= len(self.tabs):
            self.active_tab = len(self.tabs)


    def click_element(self, by: By, value: str) -> None:
        element = self.find_element(by, value)
        if element:
            element.click()


    def find_element(self, by: By, value: str) -> SeleniumWebElement:
        return self.driver.find_element(by, value)


    def write_in_element(self, by: By, value: str, text: str) -> None:
        element = self.find_element(by, value)
        if element:
            element.send_keys(text)


    def get_text(self, by: By, value: str) -> str:
        element = self.find_element(by, value)
        return element.text


    def get_title(self, by: By, value: str) -> str:
        return self.driver.title


    def get_url(self) -> str:
        return self.driver.current_url
    

    def quit_driver(self) -> None:
        self.driver.quit()
        self.driver = None
        self.tabs = []
        self.active_tab = 0