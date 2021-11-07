

class BasePage:
    def __init__(self, driver, url, timeout=3):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        self.driver.get(self.url)
