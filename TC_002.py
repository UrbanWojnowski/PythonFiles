from selenium.webdriver import Chrome
import TakeScreenshoot
path = "C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.maximize_window()
mainWin=""
driver.get("https://www.naukri.com")
Allwindow = driver.window_handles
for win in Allwindow:
    driver.switch_to.window(win)
    # keep oryginal window and close all the other popups
    # print(driver.current_url)
    if driver.current_url == "https://www.naukri.com/":
        mainWin = win
    else:
        driver.close()
driver.switch_to.window(mainWin)
print(driver.current_url)


