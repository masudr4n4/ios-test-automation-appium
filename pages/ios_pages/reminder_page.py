from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from utils.locators.ios_locators import *
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

class ReminderPage(PageFactory):
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.home_locator = HomepageLocators
        self.fake = Faker()

    def add_new_list(self):
        name = self.fake.word()
        self.driver.find_element(*self.home_locator.ADD_LIST_BTN).click()
        self.driver.find_element(*self.home_locator.LIST_NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.home_locator.DONE_BTN).click()

        return name

    def get_list_name(self,name):
        try:
            return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.home_locator.LIST_NAME[1].format(name)))
        )
        except (NoSuchElementException,TimeoutException):
            return None

    def click_list_options(self):
        self.driver.find_element(*self.home_locator.MORE_OPTION_BTN).click()

    def delete_list(self):
        self.driver.find_element(*self.home_locator.DELETE_LIST).click()

    def return_to_lists(self):
        self.driver.find_element(*self.home_locator.LISTS_BTN).click()

    def open_new_list_item(self,item):
        self.driver.find_element(By.XPATH, self.home_locator.ITEM_ON_HOMEPAGE[1].format(item)).click()