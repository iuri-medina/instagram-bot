from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import csv


browser = webdriver.Chrome("./chromedriver.exe")


# navigate to Instagram
browser.get('https://www.instagram.com')

# put your username and password bellow
username_input = '****your username****'
password_input = '****your password****'


# puts your login information into instagram
username = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
username.send_keys('{}'.format(username_input))

password = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
password.send_keys('{}'.format(password_input))


# waits until login button and clicks on it
btn_login = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
btn_login.click()


# passes by the saving information screen
btn_salvar_info = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
btn_salvar_info.click()

# passes by the notification screen
btn_ativar_notif = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))
btn_ativar_notif.click()


# goes to your account page
browser.get("https://instagram.com/{}".format(username_input))


# goes to the list of the followers
followers_list = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')))
followers_list.click()


sleep(5)


# scrolls all the way through the list until hit bottom
def scroll(timeout):
    scroll_pause_time = timeout
    last_height = browser.execute_script("return document.querySelector('div.isgrP').scrollHeight")
    i = 0
    while True:
        browser.execute_script(
            "document.querySelector('div.isgrP').scrollTo(0, document.querySelector('div.isgrP').scrollHeight);")
        sleep(scroll_pause_time)
        new_height = browser.execute_script("return document.querySelector('div.isgrP').scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        i = i + 1


scroll(5)

# gets the followers names
followers = browser.find_elements_by_css_selector('a.FPmhX')

print('you have {} followers'.format(len(followers)))


# create a csv file with all the followers names enumerated
with open('followers_list.csv', 'w') as f:
    csv_file = csv.writer(f)
    csv_file.writerow(["follower number", "follower full name"])


for i, follower in enumerate(followers):
    with open('followers_list.csv', 'a') as f:
        csv_file = csv.writer(f)
        csv_file.writerow(["follower {}".format(i), follower.text])

    print(follower.text)

