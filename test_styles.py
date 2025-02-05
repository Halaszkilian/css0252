import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestStyles(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("file:///path/to/styled_text.html")  # Cseréld ki a helyes fájl elérési úttal
    
    def test_heading_styles(self):
        driver = self.driver
        h1 = driver.find_element(By.TAG_NAME, "h1")
        self.assertEqual(h1.value_of_css_property("color"), "rgb(0, 128, 0)")  # Zöld
        self.assertEqual(h1.value_of_css_property("font-size"), "28px")
        
        h2 = driver.find_element(By.TAG_NAME, "h2")
        self.assertEqual(h2.value_of_css_property("color"), "rgb(0, 0, 128)")  # Navy
        self.assertEqual(h2.value_of_css_property("font-size"), "24px")
    
    def test_list_styles(self):
        driver = self.driver
        nested_list = driver.find_element(By.CSS_SELECTOR, "ul ul")
        self.assertEqual(nested_list.value_of_css_property("color"), "rgb(0, 0, 255)")  # Kék
    
    def test_italic_text(self):
        driver = self.driver
        italic_items = driver.find_elements(By.CLASS_NAME, "italic")
        for item in italic_items:
            self.assertEqual(item.value_of_css_property("font-style"), "italic")
            self.assertEqual(item.value_of_css_property("color"), "rgb(0, 0, 255)")  # Kék
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
