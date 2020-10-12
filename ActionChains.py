from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path="C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")

driver.find_element_by_name("fld_username").send_keys("Hello")

act = ActionChains(driver)
# perform TAB key
# act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys('a').perform()
time.sleep(5)

#act.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(Keys.DELETE).perform()


