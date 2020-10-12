from selenium.webdriver import Chrome
import TakeScreenshoot
path = "C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
driver.get("http://www.theTestingWorld.com/testings")
#TakeScreenshoot.take_screenshot(driver,"pic1")
#Scrolling down js
driver.execute_script("window.scrollTo(0,400);")