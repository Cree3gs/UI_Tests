from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @property
    def donate_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//a[contains(@class, 'donate-button')]")

    @property
    def donate_title_1(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row1')]")

    @property
    def donate_title_2(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row2')]")

    @property
    def donate_title_3(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row3')]")

    @property
    def donate_title_4(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row4')]")

    @property
    def donate_title_5(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row5')]")

    @property
    def donate_title_6(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row6')]")

    @property
    def donate_title_7(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row7')]")

    @property
    def donate_title_8(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row8')]")

    @property
    def donate_title_9(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row contribution_amount-row9')]")

    @property
    def donate_title_text_1(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row1')]//span[contains(@class, "
                                                  "'crm-price-amount-amount')]")

    @property
    def donate_title_text_2(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row2')]//span[contains(@class, "
                                                  "'crm-price-amount-amount')]")

    @property
    def donate_title_text_3(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row3')]//span[contains(@class, "
                                                  "'crm-price-amount-amount')]")

    @property
    def donate_title_text_4(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row4')]//span[contains(@class, "
                                                  "'crm-price-amount-amount')]")

    @property
    def donate_title_text_5(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row5')]//span[contains(@class, "
                                                  "'crm-price-amount-amount')]")

    @property
    def donate_title_text_6(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row6')]//label[contains(@for, "
                                                  "'CIVICRM_QFID_18_price_4')]")

    @property
    def donate_title_text_7(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row7')]//span[contains(@class, "
                                                  "'crm-price-amount-amount')]")

    @property
    def donate_title_text_8(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row8')]//span[contains(@class, "
                                                  "'crm-price-amount-amount')]")

    @property
    def donate_title_text_9(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'price-set-row "
                                                  "contribution_amount-row9')]//label[contains(@for, "
                                                  "'CIVICRM_QFID_0_price_4')]")

    @property
    def contribution_amount(self) -> WebElement:
        return self.driver.find_element(By.XPATH, """//input[contains(@price, '["price_4","50||"]')]""")

    @property
    def contribution_amount_text(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'content calc-value')]")

    @property
    def other_amount(self) -> WebElement:
        return self.driver.find_element(By.XPATH, """//input[contains(@price, '["price_4","0"]')]""")

    @property
    def other_amount_text(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//div[contains(@class, 'content calc-value')]")

    @property
    def amount(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[contains(@name, 'price_47')]")

    @property
    def regular_checkbox(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "// input[contains( @ id, 'is_recur')]")

    @property
    def regular_amount(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//select[contains(@class, 'crm-form-select required')]")

    @property
    def e_mail(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[contains(@name, 'email-5')]")

    @property
    def name(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "//input[contains(@id, 'nick_name')]")

    @property
    def done_button(self) -> WebElement:
        return self.driver.find_element(By.XPATH, "// button[contains( @ name, '_qf_Main_upload')]")


def open_pyton_page() -> WebDriver:
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
    driver.get("https://www.python.org/")
    return driver


def open_donation_form() -> WebDriver:
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
    driver.get("https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2")
    return driver


def test_donation_title_and_amount_point():
    driver = open_pyton_page()
    main_page = MainPage(driver)
    main_page.donate_button.click()
    assert main_page.donate_title_1.is_displayed(), "Price-set-row 1 is not displayed"
    assert main_page.donate_title_text_1.text == "$ 10.00", "The text does not match"
    assert main_page.donate_title_2.is_displayed(), "Price-set-row 2 is not displayed"
    assert main_page.donate_title_text_2.text == "$ 50.00", "The text does not match"
    assert main_page.donate_title_3.is_displayed(), "Price-set-row 3 is not displayed"
    assert main_page.donate_title_text_3.text == "$ 99.00", "The text does not match"
    assert main_page.donate_title_4.is_displayed(), "Price-set-row 4 is not displayed"
    assert main_page.donate_title_text_4.text == "$ 150.00", "The text does not match"
    assert main_page.donate_title_5.is_displayed(), "Price-set-row 5 is not displayed"
    assert main_page.donate_title_text_5.text == "$ 250.00", "The text does not match"
    assert main_page.donate_title_6.is_displayed(), "Price-set-row 6 is not displayed"
    assert main_page.donate_title_text_6.text == "Basic - $ 5.00", "The text does not match"
    assert main_page.donate_title_7.is_displayed(), "Price-set-row 7 is not displayed"
    assert main_page.donate_title_text_7.text == "$ 500.00", "The text does not match"
    assert main_page.donate_title_8.is_displayed(), "Price-set-row 8 is not displayed"
    assert main_page.donate_title_text_8.text == "$ 1,000.00", "The text does not match"
    assert main_page.donate_title_9.is_displayed(), "Price-set-row 9 is not displayed"
    assert main_page.donate_title_text_9.text == "Other Amount", "The text does not match"
    main_page.contribution_amount.click()
    assert main_page.contribution_amount_text.text == "$ 50.00", "The text does not match"
    main_page.other_amount.click()
    assert main_page.other_amount_text.text == "$ 0.00", "The text does not match"


def test_donation_form():
    driver = open_donation_form()
    main_page = MainPage(driver)
    main_page.amount.clear()
    main_page.amount.send_keys("52.99")
    main_page.regular_checkbox.click()
    assert main_page.regular_amount.text == " month\n year", "The text does not match"
    main_page.e_mail.clear()
    main_page.e_mail.send_keys("Nikitatarakanow@ya.ru")
    main_page.name.clear()
    main_page.name.send_keys("Volkodaw")
    main_page.done_button.click()


if __name__ == '__main__':
    test_donation_title_and_amount_point()
    test_donation_form()
