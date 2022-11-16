from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
url = "https://mindful.care/"
faq_page  = "/html/body/div[1]/footer/div[3]/div[2]/div[2]/a"

but_expand_age = "/html/body/main/div/section[2]/details[8]/summary/div/span"
butt_expected_age_psychiatric_services = "Psychiatric Services (Medication Management) - Ages 18+"
butt_expected_therapy_services = "Therapy Services (Individual and Group Therapy) - Ages 18+"
butt_expected_substance_use_counseling = "Substance Use Counseling - Ages 18+"
age_of_psychiatric_services = "/html/body/main/div/section[2]/details[8]/div/p[1]"
age_of_therapy_services = "/html/body/main/div/section[2]/details[8]/div/p[2]"
age_of_substance_use_counseling = "/html/body/main/div/section[2]/details[8]/div/p[3]"

but_expand_person_and_virtually = "/html/body/main/div/section[2]/details[7]/summary/div/span"
expected_text = "Currently, all patient visits are virtual and in person at any of our locations"


class FAQ_page:
    """class for page Frequently Asked Questions"""
    def faqpage(self):
        pyautogui.moveTo(100, 100, duration = 1)
        driver.get(url)
        driver.find_element(By.XPATH, faq_page).click()
        pyautogui.moveTo(1000, 1000, duration = 1)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

    def click_age(self):
        """What ages do you see?"""
        driver.find_element(By.XPATH, but_expand_age ).click()

    def psychiatric_services(self):
        age_of_ps = driver.find_element(By.XPATH, age_of_psychiatric_services).text
        return age_of_ps


    def therapy_services(self):
        assert_text = driver.find_element(By.XPATH, age_of_therapy_services).text
        if assert_text == butt_expected_therapy_services:
            print("Same ages")
            return True
        else:
            driver.get_screenshot_as_file("screenshot.png")
            print("Age is not matches requirements")

    def substance_use_counseling(self):
        assert_text = driver.find_element(By.XPATH, age_of_substance_use_counseling).text
        if assert_text == butt_expected_substance_use_counseling:
            print("Same ages")
            return True
        else:
            driver.get_screenshot_as_file("screenshot.png")
            print("Age is not matches requirements")

    def click_person_virtually(self):
        """Will I be seen in-person or virtually?"""
        driver.find_element(By.XPATH, but_expand_person_and_virtually).click()

    def inperson_virtually(self):
        assert_text = driver.find_element(By.XPATH, but_expand_person_and_virtually).click()
        if assert_text == expected_text:
            print("actual result matches expected result")
            return True
        else:
            driver.get_screenshot_as_file("screenshot_in_person_virtually.png")
            print(f"actual result is not matches expected result")

    def close(self):
        time.sleep(2)
        driver.close()