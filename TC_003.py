from selenium.webdriver import Chrome
# STEP 1
import logging
path = "C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
driver = Chrome(executable_path=path)


# STEP 2
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# STEP 3
warn = logging.FileHandler('Warning_logs.txt')
warn.setLevel(logging.WARNING)

info = logging.FileHandler('Info_logs.txt')
info.setLevel(logging.INFO)

# STEP 4 create a logging format
formatter = logging.Formatter('%(acstime)s - %(name)s - %(levelname)s - %(message)s')

# STEP 5
warn.setFormatter(formatter)
info.setFormatter(formatter)

driver.maximize_window()
driver.get("http://www/thetestingworld.com/testings")
log.info("[ My URL is Opened ]")
log.warn(" [There is delay in opening of  ]")