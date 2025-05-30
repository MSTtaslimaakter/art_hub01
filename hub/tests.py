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
        # Go to the login page
        self.browser.get(f'{self.live_server_url}/log_in/')

        # Wait for the username input to appear
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )

        # Enter login credentials
        self.browser.find_element(By.NAME, 'username').send_keys('testuser')
        self.browser.find_element(By.NAME, 'password').send_keys('testpass')

        # Submit the form
        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        # Wait for the redirected page to load
        WebDriverWait(self.browser, 120).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )

        # Check if login was successful (adjust "Profile" as per your profile page content)
        self.assertIn("Profile", self.browser.page_source)
