from .base_page import BasePage
from .locators import ConsumptionsPageLocators
from .locators import LkPageLocators


class LkPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    def go_to_send_consumption_section(self):
        self.driver.find_element(*LkPageLocators.FILL_CONSUMPTION).click()

    def get_old_data(self):
        old_data = {
            "cold_water": float(self.get_cold_water_old_data()),
            "hot_water": float(self.get_hot_water_old_data()),
            "electricity": float(self.get_electricity_old_data()),
            "heat": float(self.get_heating_old_data()),
        }
        return old_data

    def get_heating_old_data(self):
        return self.driver.find_element(*ConsumptionsPageLocators.HEATING_OLD).text

    def get_hot_water_old_data(self):
        return self.driver.find_element(*ConsumptionsPageLocators.HOT_WATER_OLD).text

    def get_cold_water_old_data(self):
        return self.driver.find_element(*ConsumptionsPageLocators.COLD_WATER_OLD).text

    def get_electricity_old_data(self):
        return self.driver.find_element(*ConsumptionsPageLocators.ELECTRICITY_OLD).text

    def fill_new_data(self, data):
        pass

    def send_new_data(self):
        pass


