import base64
import os
import random

import allure
from selenium.webdriver.common.by import By

from generator.generator import generated_file
from pages.base_page import BasePage


class UploadAndDownloadPage(BasePage):
    UPLOAD_FILE = (By.CSS_SELECTOR, "input[id='uploadFile']")
    UPLOADED_FILE_PATH = (By.CSS_SELECTOR, "p[id='uploadedFilePath']")
    DOWNLOAD_FILE = (By.CSS_SELECTOR, "a[id='downloadButton']")

    @allure.step("Upload file")
    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_present(self.UPLOAD_FILE).send_keys(path)
        os.remove(path)
        uploaded_file_path_text = self.element_is_present(self.UPLOADED_FILE_PATH).text
        return file_name.split("\\")[-1], uploaded_file_path_text.split("\\")[-1]

    @allure.step("Download file")
    def download_file(self):
        link = self.element_is_present(self.DOWNLOAD_FILE).get_attribute('href')
        link_b = base64.b64decode(link)
        path_name_file = \
            rf"C:\code\test\pythonCode\pythonProject\ui_pytest_framework\filetest{random.randint(0, 999)}.jpeg"
        with open(path_name_file, "wb+") as f:
            offset = link_b.find(b"\xff\xd8")
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file)
        return check_file
