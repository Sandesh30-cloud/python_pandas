import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.youtube.com")
        # self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "search_query")
        elem.send_keys("uniitest in python")
        elem.send_keys(Keys.ENTER)
        time.sleep(5) 

        self.assertNotIn("No results found.", driver.page_source)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()