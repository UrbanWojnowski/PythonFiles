from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)

driver.get("http://www.theTestingWorld.com/testings")

# Maximize driver
driver.maximize_window()

print("Title of this page is: " + driver.title)

# fetch url

print("The URL of this page is: " + driver.current_url)

# fetch complete page html

print("********" * 10)
print(driver.page_source)
