from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


# def test_all_in_one(provided_driver: webdriver):
#     driver = provided_driver
#     user_agent = get_browser_name(driver.execute_script("return navigator.userAgent;"))
#     print("\n-----------------------------------------------------")
#     print("Test Started for WebDriver: ", user_agent)
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#     driver.find_element(by=By.ID, value="my-text-id").send_keys("This is a short Test Sentence.")
#     driver.find_element(by=By.NAME, value="my-password").send_keys("NotAPassword")
#     driver.find_element(by=By.NAME, value="my-textarea").send_keys("This is a Test From PyCharm running on Selenium.")
#
#     assert driver.find_element(by=By.ID, value="my-text-id").get_attribute('value') == "This is a short Test Sentence."
#
#     select = Select(driver.find_element(by=By.NAME, value="my-select"))
#     # select by visible text
#     select.select_by_visible_text('Three')
#     # select by index
#     select.select_by_index(2)
#
#     driver.find_element(by=By.NAME, value="my-datalist").send_keys("Test_Data_List")
#     driver.find_element(by=By.ID, value="my-radio-2").click()
#     driver.implicitly_wait(10)
#     driver.find_element(by=By.NAME, value="my-colors").send_keys("#40E0D0")
#     date = driver.find_element(by=By.NAME, value="my-date")
#     date.send_keys("03/26/2024")
#     action = webdriver.common.action_chains.ActionChains(driver)  # for removing the hover
#     action.move_to_element_with_offset(date, 100, 100)
#     action.click()
#     action.perform()
#     driver.implicitly_wait(10)
#     driver.find_element(by=By.NAME, value="my-range").send_keys("9")
#     driver.save_screenshot("Screenshots/image_" + user_agent + ".png")
#
#     driver.close()
#     driver.quit()
#     print("Test Completed for WebDriver: ", user_agent)
#     print("-----------------------------------------------------")


def test_all_in_one_edge():
    driver = webdriver.ChromiumEdge()
    browser_main_logic(driver)


def test_all_in_one_chrome():
    driver = webdriver.Chrome()
    browser_main_logic(driver)


def test_all_in_one_firefox():
    driver = webdriver.Firefox()
    browser_main_logic(driver)


def browser_main_logic(preferred_driver: webdriver):
    driver = preferred_driver
    user_agent = get_browser_name(driver.execute_script("return navigator.userAgent;"))
    print("\n-----------------------------------------------------")
    print("Test Started for WebDriver: ", user_agent)
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    driver.find_element(by=By.ID, value="my-text-id").send_keys("This is a short Test Sentence.")
    driver.find_element(by=By.NAME, value="my-password").send_keys("NotAPassword")
    driver.find_element(by=By.NAME, value="my-textarea").send_keys("This is a Test From PyCharm running on Selenium.")

    select = Select(driver.find_element(by=By.NAME, value="my-select"))
    # select by visible text
    select.select_by_visible_text('Three')
    # select by index
    select.select_by_index(2)

    driver.find_element(by=By.NAME, value="my-datalist").send_keys("Test_Data_List")
    driver.find_element(by=By.ID, value="my-radio-2").click()
    driver.implicitly_wait(10)
    driver.find_element(by=By.NAME, value="my-colors").send_keys("#40E0D0")

    date = driver.find_element(by=By.NAME, value="my-date")
    date.send_keys("03/26/2024")
    action = webdriver.common.action_chains.ActionChains(driver)  # for removing the hover
    action.move_to_element_with_offset(date, 100, 100)
    action.click()
    action.perform()
    driver.implicitly_wait(10)
    driver.find_element(by=By.NAME, value="my-range").send_keys("9")
    driver.save_screenshot("Screenshots/image_" + user_agent + ".png")

    assert driver.find_element(by=By.ID, value="my-text-id").get_attribute('value') == "This is a short Test Sentence."
    assert driver.find_element(by=By.NAME, value="my-password").get_attribute('value') == "NotAPassword"
    assert driver.find_element(by=By.NAME, value="my-textarea").get_attribute(
        'value') == "This is a Test From PyCharm running on Selenium."

    assert driver.find_element(by=By.NAME, value="my-colors").get_attribute(
        'value').upper() == "#40E0D0"

    driver.close()
    driver.quit()
    print("Test Completed for WebDriver: ", user_agent)
    print("-----------------------------------------------------")


def get_browser_name(user_agent_string):
    if "Edg" in user_agent_string:
        return "Edge"
    elif "Chrome" in user_agent_string:
        return "Chrome"
    elif "Gecko" in user_agent_string:
        return "Firefox"
    else:
        return "Unknown"
