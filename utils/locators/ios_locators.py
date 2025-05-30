from appium.webdriver.common.appiumby import By,AppiumBy

class HomepageLocators:
    CONTINUE_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="Continue"]')
    NEW_REMINDER = (By.XPATH,'//XCUIElementTypeButton[@name="New Reminder"]')
    REMINDER_TITLE = (By.XPATH,'//XCUIElementTypeButton[@name="Title"]')
    DONE_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="Done"]')
    LIST_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="List"]')
    LISTS_BTN = (By.XPATH, '//XCUIElementTypeButton[@name="Lists"]')
    ADD_LIST_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="Add List"]')
    LIST_NAME_INPUT = (By.XPATH,'//XCUIElementTypeTextField[@name="List Name"]')
    LIST_NAME = (By.XPATH,'//XCUIElementTypeStaticText[@name="{}"]')
    DELETE_BTN = (By.XPATH,'//XCUIElementTypeStaticText[@name="Delete"]')
    DELETE_LIST = (By.XPATH,'//XCUIElementTypeButton[@name="Delete List"]')
    CONFIRM_DELETE = (By.XPATH,'//XCUIElementTypeButton[@name="Delete"]')
    ITEM_ON_HOMEPAGE = (By.XPATH,'//XCUIElementTypeStaticText[@name="{}"]')
    EDIT_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="Edit"]')
    MORE_OPTION_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="More"]')
    SHOW_LIST_INFO = (By.XPATH,'//XCUIElementTypeButton[@name="Show List Info"]')
    CANCEL_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="Cancel"]')
    REMOVE_LIST_ITEM = (By.XPATH,'//XCUIElementTypeButton[@name="Remove {}"]')

    SCHEDULED_BTN= (By.XPATH,'//XCUIElementTypeButton[@name="Scheduled, 0 reminders"]')
    TOMORROW_BTN = (By.XPATH,'//XCUIElementTypeOther[@name="Tomorrow" and @label="Tomorrow"]')
    TOMORROW_REMINDER_TITLE = (By.XPATH,'//XCUIElementTypeOther[@name="Horizontal scroll bar, 1 page"][5]')
    ADD_NOTED_BTN = (By.XPATH,'//XCUIElementTypeOther[@name="Horizontal scroll bar, 1 page"][4]')
    SELECT_TOMORROW_REMINDER = (By.XPATH,'//XCUIElementTypeButton[@name="circle"][2]')
    BACK_TO_LIST = (By.XPATH,'//XCUIElementTypeButton[@name="Back to list"]')
    REMINDER_COUNTER = (By.XPATH,'(//XCUIElementTypeCell//XCUIElementTypeStaticText)[2]')
    REMINDER_TITLE_INPUT = (By.XPATH,'//XCUIElementTypeTextField[@name="Title"]')
    REMINDER_NOTES_INPUT = (By.XPATH,'//XCUIElementTypeTextField[@name="Notes text view"]')
    REMINDER_QUICK_TITLE_INPUT = (By.XPATH,'//XCUIElementTypeTextField[@name="Quick Entry Title Field"]')
    ADD_BTN = (By.XPATH,'//XCUIElementTypeButton[@name="Add"]')
    LOCAL_LIST = (By.XPATH,'//XCUIElementTypeStaticText[@name="List"]')
    LOCAL_LIST_ITEM = (By.XPATH,'(//XCUIElementTypeStaticText[@name="{}"])[2]')
