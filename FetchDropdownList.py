from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)

driver.get("http://www.theTestingWorld.com/testings")

# Maximize driver
driver.maximize_window()

# DropDown
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")

#Fetch of selected option
print(obj.first_selected_option.text)

for op in obj.options:
    print(op.text)