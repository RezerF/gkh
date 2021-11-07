from selenium import webdriver
from selenium.webdriver.common.by import By


class AuthPageLocators:
    LOGIN = By.XPATH, '//input[@name="ls"]'
    PASS = By.XPATH, '//input[@name="pwd"]'
    SUBMIT_BUTTON = By.XPATH, '//button[@class="btn btn-primary showAllBtn button-auth"]'
