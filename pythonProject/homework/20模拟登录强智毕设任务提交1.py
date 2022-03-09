import io
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.remote.command import Command


def add_cookie(self, cookie_dict):

    self.execute(Command.ADD_COOKIE, {'cookie': cookie_dict})


userName='600135'
pwd='600135.Jxf'
# 改变标准输出的默认编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# 创建chrome参数对象
option = ChromeOptions()
# 把chrome设置成无界面模式，不论windows还是linux都可以，自动匹配
# option.add_argument("--headless")  # 指定无头模式
driver = webdriver.Chrome(options=option)
driver.set_window_size(1920, 1080)
# 登录页面
url = r'https://webvpn.jsu.edu.cn/'
headers1={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0'}
# 访问登录页面
driver.get(url)
# 等待一定时间，让js脚本加载完毕
driver.implicitly_wait(3)
# 输入用户名
usernameTextBox = driver.find_element(By.CLASS_NAME, 'el-input__inner')
usernameTextBox.send_keys(userName)
# 输入密码
password = driver.find_element(By.XPATH, "//*[@type='password']")
password.send_keys(pwd)
# 点击“登录”按钮
login_frame = driver.find_element(By.XPATH,"//*[@class='login-frame-left-below-div2']")
login_button=login_frame.find_element(By.XPATH, "//*[@class='el-button el-button--primary' and @type='button']")
print(login_button)
# 获取当前页面 cookie
print(driver.get_cookies())
login_button.send_keys(Keys.RETURN)
driver.implicitly_wait(5)

print('driver.current_url   :!!! ')
print(driver.current_url)
print('# 窗口句柄 看看现在打开的窗口有什么')
print(driver.window_handles)  # 窗口句柄 看看现在打开的窗口有什么
# driver.switch_to.window(driver.window_handles[1]) # 切换窗口
# 网页截图
driver.save_screenshot(os.getcwd() + r'\data\000.png')

print('\n强智教务系统入口： ')
强智入口=driver.find_element(By.LINK_TEXT, "强智教务系统（师生入口）")
# driver.find_element(By.LINK_TEXT, "正方OA").click()
print('\n强智教务系统入口： ')
强智入口.click()
driver.implicitly_wait(0.5)
强智入口.click()
driver.implicitly_wait(5)
driver.save_screenshot(os.getcwd() + r'\data\002.png')#改改改
driver.switch_to.window(driver.window_handles[1]) # 切换窗口
driver.find_element(By.XPATH,"/html/body/div[6]/a[1]/div/div[2]").click() #查看个人课表


