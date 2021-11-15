from selenium import webdriver
from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOGIN = By.XPATH, '//input[@name="ls"]'
    PASS = By.XPATH, '//input[@name="pwd"]'
    SUBMIT_BUTTON = By.XPATH, '//button[@class="btn btn-primary showAllBtn button-auth"]'


class LkPageLocators:
    FILL_CONSUMPTION = By.XPATH, '//*[@id="navbar"]/div[2]/ul/li[3]/a'


class ConsumptionsPageLocators:
    HEATING_OLD = By.XPATH, "//*[text()[contains(.,'Заводской номер: 22178791')]]/div/div[2]"
    COLD_WATER_OLD = By.XPATH, "//*[text()[contains(.,'Заводской номер: 1018019845405')]]/div/div[2]"
    HOT_WATER_OLD = By.XPATH, "//*[text()[contains(.,'Заводской номер: 1018017407209')]]/div/div[2]"
    ELECTRICITY_OLD = By.XPATH, "//*[text()[contains(.,'Заводской номер: 34915743')]]/div/div[2]"

    HEATING_INPUT = By.XPATH, '//*[@id="sch_399022_num_1"]'
    COLD_WATER_INPUT = By.XPATH, '//*[@id="sch_399025_num_3"]'
    HOT_WATER_INPUT = By.XPATH, '//*[@id="sch_399023_num_2"]'
    ELECTRICITY_INPUT = By.XPATH, '//*[@id="sch_399026_num_4"]'

    SEND_BUTTON = By.XPATH, '//*[@class="btn btn-primary mediumBtn lkBtn"]'
