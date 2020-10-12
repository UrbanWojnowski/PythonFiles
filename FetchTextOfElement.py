from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)

driver.get("http://www.theTestingWorld.com/testings")

# Maximize driver
driver.maximize_window()

# Fetch element text
print("Text on link is: " +driver.find_element_by_class_name("displayPopup").text)

#Fettching attrinute value of Element

print("Value of attribute: " + driver.find_element_by_xpath("//input[@type='submit']").get_attribute("value"))