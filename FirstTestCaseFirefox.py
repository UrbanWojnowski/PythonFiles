from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select
path="C:\\Users\\ugwoj\\Downloads\\geckodriver-v0.27.0-win64\\geckodriver.exe"
driver = Firefox(executable_path=path)

driver.get("http://www.theTestingWorld.com/testings")

# Maximize driver
driver.maximize_window()

# Enter data to the textBox
driver.find_element_by_name("fld_username").send_keys("HelloWorld")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("data@gmail.com")
driver.find_element_by_name("fld_password").send_keys("abcd123")
driver.find_element_by_name("fld_cpassword").send_keys("abc123")
driver.find_element_by_name("fld_username").clear()
driver.find_element_by_name("fld_username").send_keys("abc123")

# Working on the radio button
driver.find_element_by_xpath("//input[@value='home']").click()

# Working on the Chceckbox
driver.find_element_by_name("terms").click()

# Work on Button
# driver.find_element_by_xpath("//input[@type='submit']").click()

# links
# driver.find_element_by_link_text("Read Detail").click()

# Work on dropdown 1 approach
#obj = Select(driver.find_element_by_name("sex"))
#obj.select_by_index(1)

#dropdown 2 approach
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_value("2")


# Closing browser
#driver.close()
