from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

User = get_user_model()

class FunctionalTest(StaticLiveServerTestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_login(self):
        self.browser.get(f'{self.live_server_url}/log_in/')
        WebDriverWait(self.browser, 240).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        self.browser.find_element(By.NAME, 'username').send_keys('testuser')
        self.browser.find_element(By.NAME, 'password').send_keys('testpass')
        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        WebDriverWait(self.browser, 240).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        self.assertIn("Profile", self.browser.page_source)

    