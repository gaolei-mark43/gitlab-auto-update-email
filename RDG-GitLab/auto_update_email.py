import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import sys

# 读取文件new_users.txt
def read_new_users():
    new_users = []
    with open("new_users.txt", "r") as f:
        users = f.readlines()
        if len(users) == 0:
            print("文件为空，推出程序")
            sys.exit(1)
        for user in users:
            user = user.strip("\n")
            new_users.append(user)
    return new_users



def modify_user_email(name):
    start_time = time.time()
    time.sleep(5)
    # 设置FirefoxOptions对象
    options = Options()
    options.binary_location = 'C:\\ProgramData\\firefox.exe'

    # 设置GeckoDriver路径
    gecko_driver_path = 'D:\geckodriver.exe'

    # 创建Firefox浏览器实例
    driver = webdriver.Firefox(service=Service(gecko_driver_path), options=options)

    driver.get('https://gitlab.test.com/')
    driver.implicitly_wait(5)

    button = driver.find_element(By.ID, "oauth-login-cas3")
    button.click()

    input_box = driver.find_element(By.XPATH, "//input[@class='user-input']")
    input_box.clear()
    input_box.send_keys("leigao6") #gitlab超管域账号

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('XXXXXX') #gitlab超管域账号密码

    password_input.send_keys(Keys.ENTER)

    # 睡眠
    time.sleep(2)
    driver.get('https://gitlab.test.com/admin/users')
    print("开始查询")
    time.sleep(1)
    driver.get('https://gitlab.test.com/admin/users')


    input_box = driver.find_element(By.XPATH, "//input[@id='search_query']")
    input_box.clear()  # 清空输入框
    input_box.send_keys("{}".format(name))
    time.sleep(2)
    input_box.send_keys(Keys.ENTER)
    time.sleep(2)


    xpath_string = "//span[@class='gl-avatar-labeled-label' and text()='bczhang9']"
    xpath_string = xpath_string.replace("bczhang9", name)

    element = driver.find_element(By.XPATH, xpath_string)
    time.sleep(2)

    element.click()

    element = driver.find_element(By.XPATH, "//a[@data-testid='edit']")

    element.click()

    driver.get('https://gitlab.test.com/admin/users/{}/edit'.format(name))

    input_box = driver.find_element(By.ID, "user_email")

    input_box.clear()

    input_box.send_keys("{}@ilfytek.com".format(name))
    wait = WebDriverWait(driver, 2)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='commit'][value='Save changes']")))

    # 模拟点击操作
    element.click()
    driver.get('https://gitlab.test.com/admin/users/{}/edit'.format(name))
    input_box = driver.find_element(By.ID, "user_email")

    input_box.clear()

    input_box.send_keys("{}@qq.com".format(name))
    wait = WebDriverWait(driver, 2)
    element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='commit'][value='Save changes']")))

    # 模拟点击操作
    element.click()

    driver.get('https://gitlab.test.com/admin/users/{}/edit'.format(name))
    input_box = driver.find_element(By.ID, "user_email")

    input_box.clear()

    input_box.send_keys("{}@iflytek.com".format(name))
    wait = WebDriverWait(driver, 2)
    element = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'][name='commit'][value='Save changes']")))

    # 模拟点击操作
    element.click()


    time.sleep(3)

    end_time = time.time()
    # 关闭浏览器
    driver.quit()
    print("{}本次配置耗时：".format(name), end_time - start_time, "秒")


if __name__ == '__main__':
    new_users = read_new_users()
    for user in new_users:
        modify_user_email(user)