import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_longest_substring_ui(self):
        driver = self.driver
        driver.get("https://dummy-agrichain.com")  # fake site just for demo

        input_box = driver.find_element(By.ID, "stringInput")
        input_box.send_keys("abcabcbb")

        submit_btn = driver.find_element(By.ID, "submitBtn")
        submit_btn.click()

        result = driver.find_element(By.ID, "result").text
        self.assertIn("3", result)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
