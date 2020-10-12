from selenium.webdriver import Chrome
import pytest

@pytest.fixture(scope="module")
def setPath():
    global driver
    path = "C:\\Users\\ugwoj\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    yield
    driver.close()

#@pytest.mark.skipif(a>100,reason = "Stop execution")
#@pytest.mark.skip("Don't want to execute on current build")
#@pytest.mark.Smoke
def test_registration_valid_data(setPath):

    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    assert driver.title == "Login & Sign Up Forms"

#@pytest.mark.Sanity
def test_registration_invalid_data(setPath):

    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    assert driver.current_url == "http://www.theTestingWorld.com/testings/register.php"

def test_closing_invalid_data(setPath):

    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()


