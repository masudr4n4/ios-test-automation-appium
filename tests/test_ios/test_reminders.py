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

    @allure.title("Verify adding reminder to new list and delete")
    @allure.step("Verify adding reminder to new list and delete")
    @allure.description("Verify adding reminder to new list and delete")
    @pytest.mark.regression
    def test_add_reminder_to_lists(self):
        reminder_to_add = 2
        homepage = ReminderPage(self.driver)
        new_list_name = homepage.add_new_list()
        assert homepage.get_list_name(new_list_name) is not None
        homepage.return_to_lists()
        homepage.add_reminder_to_list(new_list_name,reminder_to_add)
        homepage.open_new_list_item(new_list_name)
        assert homepage.count_reminder() == reminder_to_add
        homepage.click_list_options()
        homepage.delete_list(confirm=True)
        assert homepage.get_list_name(new_list_name) is None, "List item is not deleted"

    @allure.title("Verify Delete working as expected from home page")
    @allure.step("Test Add new list to reminders page")
    @allure.description("Adding new list to the reminders list")
    @pytest.mark.regression
    def test_delete_list_from_home(self):
        homepage = ReminderPage(self.driver)
        new_list_name = homepage.add_new_list()
        assert homepage.get_list_name(new_list_name) is not None
        homepage.return_to_lists()
        homepage.delete_new_list_from_home(new_list_name)
        assert homepage.get_list_name(new_list_name) is None, "List item is not deleted"

