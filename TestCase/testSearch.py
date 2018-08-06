import unittest
from selenium import webdriver
import time


class SearchTest(unittest.TestCase):
    '''test search functionality'''


    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_by_category(self):
        '''search category phones'''
        self.search_filed = self.driver.find_element_by_name('q')
        self.search_filed.clear()

        self.search_filed.send_keys("phones")
        self.search_filed.submit()

        products = self.driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li')
        self.assertEqual(3, len(products))

    def test_search_by_name(self):
        '''search name salt shaker'''

        self.search_filed = self.driver.find_element_by_name('q')
        self.search_filed.clear()
        self.search_filed.send_keys('salt shaker')
        self.search_filed.submit()
        time.sleep(5)

        products = self.driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li')
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)