from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec

import pytest
import time

@pytest.fixture()
def environment_setup():
    global driver
    path = "C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.refresh()
    driver.maximize_window()
    yield
    driver.close()

def test_verify_registration(environment_setup):


    # DropDown
    wait = WebDriverWait(driver,100)
    wait.until(ec.text_to_be_present_in_element(By.ID,'countryId'))
    obj = Select(driver.find_element_by_id("countryId"))
    obj.select_by_visible_text("India")

    wait.until((ec.text_to_be_present_in_element(By.ID,'stateId'),'Delhi'))
    obj = Select(driver.find_element_by_id("stateId"))
    obj.select_by_visible_text("Delhi")

    # Working on Chceckbox
  #  driver.find_element_by_name("terms").click()

    # Work on Button
  #  driver.find_element_by_xpath("//input[@type='submit']").click()

    # Work on Links
  #  driver.find_element_by_link_text("Read Detail").click()

  #  assert driver.current_url == "http://www.theTestingWorld.com/testings"