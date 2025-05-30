import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestWebPage(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_main_correct_heading(self):
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')

        # When
        heading = self.driver.find_element(By.TAG_NAME, 'h2')

        # Then
        self.assertIsNotNone(heading)
        self.assertEqual(heading.text, "Profesjonalne Rozwiązania IT dla Twojej Firmy")

    def test_portfolio_name_present(self):
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/portfolio.html')

        # When
        heading = self.driver.find_element(By.TAG_NAME, 'h1')

        # Then
        self.assertIsNotNone(heading)
        self.assertEqual(heading.text, "IT Design")

    def test_team_photos(self):
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/team.html')

        # When
        img = self.driver.find_element(By.XPATH, "//div[@class='container']/div[3]/img")

        # Then
        self.assertIsNotNone(img)
        result = img.is_displayed()
        self.assertTrue(result)

    def test_experience_font(self):
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')

        # When
        text = self.driver.find_element(By.TAG_NAME, 'p')

        # Then
        self.assertIsNotNone(text)
        self.assertEqual(text.value_of_css_property("font-size"), "18px")

    def test_copyright_year(self):
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')

        # When
        text = self.driver.find_element(By.XPATH, '//footer/p')

        # Then
        self.assertIsNotNone(text)
        self.assertEqual(text.text, "© 2024 IT Design. Wszystkie prawa zastrzeżone.")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
