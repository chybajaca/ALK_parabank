from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:

    """
    Base class for each page
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait_5s = WebDriverWait(self.driver, 5)
        self.alert = Alert(self.driver)
        self._verify_page()


    def _verify_page(self):
        self.wait_5s.until(EC.presence_of_element_located((By.XPATH, '//*[@id="rightPanel"]/h4')))
        return