from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory.Pagefactory import PageFactory
from utils.locators.ios_locators import *
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from time import sleep
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

    def delete_list(self,confirm=False):
        self.driver.find_element(*self.home_locator.DELETE_LIST).click()
        if confirm:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.home_locator.CONFIRM_DELETE)
            ).click()



    def return_to_lists(self):
        self.driver.find_element(*self.home_locator.LISTS_BTN).click()

    def open_new_list_item(self,item):
        self.driver.find_element(By.XPATH, self.home_locator.ITEM_ON_HOMEPAGE[1].format(item)).click()
    def click_add_reminder(self):
        self.driver.find_element(*self.home_locator.NEW_REMINDER).click()

    def add_reminder_to_list(self,list_item,reminder_count):
        for i in range(reminder_count):
            self.click_add_reminder()
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.home_locator.REMINDER_QUICK_TITLE_INPUT)
            ).send_keys(self.fake.word())
            self.driver.find_element(*self.home_locator.REMINDER_NOTES_INPUT).send_keys(self.fake.text())
            self.driver.find_element(*self.home_locator.LOCAL_LIST).click()
            self.driver.find_element(By.XPATH, self.home_locator.LOCAL_LIST_ITEM[1].format(list_item)).click()
            self.driver.find_element(*self.home_locator.ADD_BTN).click()
            sleep(0.5)

    def count_reminder(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.home_locator.MORE_OPTION_BTN)
        )
        return len(self.driver.find_elements(*self.home_locator.REMINDER_TITLE_INPUT))

    def delete_new_list_from_home(self,new_list_name):
        self.driver.find_element(*self.home_locator.EDIT_BTN).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.home_locator.REMOVE_LIST_ITEM[1].format(new_list_name)))
        ).click()
        delete_btn = self.driver.find_element(*self.home_locator.DELETE_BTN)

        self.driver.execute_script("mobile: tap", {"x": delete_btn.location['x'] + 50, "y": delete_btn.location['y'] + 50})
        self.driver.find_element(*self.home_locator.DONE_BTN).click()


