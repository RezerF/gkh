from pages import auth_page
from pages import lk_page
import calculate


def test_1(driver):
    new_data = calculate.get_new_data()
    url = "https://недолжник.рф"
    page = auth_page.AuthPage(url=url, driver=driver)
    page.open()
    page.authorize()
    page = lk_page.LkPage(driver, driver.current_url)
    page.go_to_send_consumption_section()
    old_data = page.get_old_data()
    consumptions = calculate.calculate_consumption(old_data, new_data)
    money = calculate.calculate_money(consumptions)
    print(money)


