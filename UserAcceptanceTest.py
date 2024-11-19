from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class GitHubLoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Mengunduh dan mengonfigurasi ChromeDriver menggunakan WebDriverManager
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()

    def test_github_title(self):
        # Mengunjungi GitHub dan memeriksa apakah judul halaman benar
        self.driver.get("https://github.com/")
        self.assertIn("GitHub", self.driver.title)

    def test_login_and_navigation(self):
        # Mengunjungi halaman login GitHub
        self.driver.get("https://github.com/login")

        # Tunggu elemen input username termuat
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.NAME, "commit")

        # Masukkan kredensial uji
        username_field.send_keys("your_username")  # Ganti dengan username uji
        password_field.send_keys("your_password")  # Ganti dengan password uji
        login_button.click()

        # Tunggu hingga halaman setelah login termuat
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "avatar"))
        )
        print("Login berhasil!")

        # Akses salah satu repository
        self.driver.get("https://github.com/your_username/your_repository")  # Ganti dengan URL repo Anda
        print("Membuka repository...")
        time.sleep(5)  # Tampilkan repository selama 5 detik

        # Akses halaman profil
        self.driver.get("https://github.com/your_username")  # Ganti dengan username Anda
        print("Membuka halaman profil...")
        time.sleep(10)  # Tampilkan profil selama 10 detik

    @classmethod
    def tearDownClass(cls):
        # Jangan tutup browser untuk memungkinkan pemeriksaan hasil pengujian
        print("Browser tidak ditutup. Periksa hasil pengujian pada browser yang terbuka.")
        # cls.driver.quit()  # Jangan tutup browser

if __name__ == "__main__":
    unittest.main()
