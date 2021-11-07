from pages import auth_page


def test_1(driver):
    url = "https://недолжник.рф"
    page = auth_page.AuthPage(url=url, driver=driver)
    page.open()
    page.authorize()
    pass
