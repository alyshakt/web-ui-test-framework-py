from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui

def write_file():
    """function for Create the file - scraped.csv, automation code open webpage https://mindful.care/frequently-asked-questions,
     return questions and answers in readable format """
    f = open("scraped.csv", "w")
    start = "/html/body/main/div/section[2]/details["
    end_a = "]/div"
    end_q = "]/summary/div/span"
    driver = webdriver.Chrome()
    url = "https://mindful.care/"
    faq_page = "/html/body/div[1]/footer/div[3]/div[2]/div[2]/a"
    pyautogui.moveTo(100, 100, duration=1)
    driver.get(url)
    driver.maximize_window()
    driver.find_element(By.XPATH, faq_page).click()

    for i in range(1, 12):
        x_path_question = start + str(i) + end_q
        # print(x_path_answer)
        question_text = driver.find_element(By.XPATH, x_path_question).text
        f.write("\n" + str(i) + ". " + question_text + "\n")
        driver.find_element(By.XPATH, x_path_question).click()
        x_path_answer = start + str(i) + end_a
        answer_el = driver.find_element(By.XPATH, x_path_answer)
        children = answer_el.find_elements(By.XPATH, "p")
        print(len(children))
        for c in children:
            print(c.text)
            f.write(c.text + "\n")


write_file()