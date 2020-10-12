
def take_screenshot(driver,name):
    driver.get_screenshot_as_file("C:\\Development\\Automation\\" + name + ".png")