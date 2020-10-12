from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path="C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com")
act = ActionChains(driver)
act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()
#act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
#act.move_to_element(driver.find_element_by_xpath("//span[text()='TUTORIAL']")).perform()
# LEft click
#act.click().perform()
# Right click
#act.context_click().perform()
#act.double_click().perform()