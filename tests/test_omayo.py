from selenium import webdriver
from selenium.webdriver.common.by import By


def test_omayo_search():

    driver = webdriver.Chrome()

    driver.get("https://omayo.blogspot.com/")

    search_box = driver.find_element(By.CSS_SELECTOR, "input[title='search'][name='q']")

    search_box.send_keys("Selenium")

    assert search_box.get_attribute("value") == "Selenium"

    driver.quit()