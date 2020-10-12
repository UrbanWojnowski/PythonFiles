from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)

driver.get("http://www.theTestingWorld.com/testings")

# Maximize driver
driver.maximize_window()

print(driver.title)

