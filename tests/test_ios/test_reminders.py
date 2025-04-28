import pytest
import allure
from pages.ios_pages.reminder_page import ReminderPage


@pytest.mark.usefixtures("setup")
class TestReminderHomePage:
    @allure.title("Verify new list adding to reminder")
    @allure.step("Test Add new list to reminders page")
    @allure.description("Adding new list to the reminders list")
    @pytest.mark.regression
    def test_add_reminder_new_list(self):
        homepage = ReminderPage(self.driver)
        new_list_name = homepage.add_new_list()
        assert homepage.get_list_name(new_list_name) is not None

    @allure.title("Verify new list adding to reminder and deleting")
    @allure.step("Test Add new list to reminders page and new list")
    @allure.description("Adding new list to the reminders list and deleting the newly added list")
    @pytest.mark.regression
    def test_add_new_list_and_delete(self):
        homepage = ReminderPage(self.driver)
        new_list_name = homepage.add_new_list()
        assert homepage.get_list_name(new_list_name) is not None
        homepage.click_list_options()
        homepage.delete_list()
        assert homepage.get_list_name(new_list_name) is None

    @allure.title("Verify open newly added list and deleting")
    @allure.step("Test Added new list shows on the home page")
    @allure.description("Newly added new list shows on the home page")
    @pytest.mark.regression
    def test_newly_added_list_shows_on_lists(self):
        homepage = ReminderPage(self.driver)
        new_list_name = homepage.add_new_list()
        assert homepage.get_list_name(new_list_name) is not None
        homepage.return_to_lists()
        homepage.open_new_list_item(new_list_name)
        homepage.click_list_options()
        homepage.delete_list()
        assert homepage.get_list_name(new_list_name) is None,"List item is not deleted"
