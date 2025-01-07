# encoding: utf-8

from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理驱动
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from browsermobproxy import Server
import time

sleep_second = 1
login_page = "http://221.199.189.180:8090/cns-bmfw-web/bmfw/bmfwnewlogin/login"
proxy_path = "/Users/jerry/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"
driver_path = "/Users/jerry/Downloads/chromedriver-mac-x64/chromedriver"


# 设置浏览器、启动浏览器
def initBrowser():
    option = Options()
    option.add_argument("--no-sandbox")
    option.add_experimental_option("detach", True)
    option.add_argument("--proxy-server=%s" % proxy.proxy)
    browser = webdriver.Chrome(
        service=Service(driver_path),
        options=option,
    )

    return browser

def get_open_url(name):
    entries = proxy.har["log"]["entries"]
    for entry in entries:
        if "request" in entry.keys():
            url = str(entry["request"]["url"])
            if name in url:
                return url

def open_window(url):
    browser.execute_script('window.open("{url}")'.format(url=url))

def close_window():
    browser.execute_script("window.close()")

def get_dept_name():
    steps = browser.find_elements(By.CLASS_NAME, "circulate-item")
    for step in steps:
        step_name, dept_name = "", ""
        try:
            step_name = step.find_element(
                By.CLASS_NAME, "circulate-step2 "
            ).get_attribute("innerHTML")
        except:
            pass
        if step_name == "区办理单位":
            try:
                dept_name = step.find_element(
                    By.CLASS_NAME, "circulate-step-label"
                ).get_attribute("innerHTML")
            except:
                pass
        if dept_name != "":
            start = dept_name.find("（")
            end = dept_name.find("）")
            return dept_name[start - 1 : end]

def logon():
    # 输入用户名密码
    username = browser.find_element(By.ID, "username")
    username.send_keys("15052600cbr01")
    psd = browser.find_element(By.ID, "psd")
    psd.send_keys("Aa123-123")
    # 点击登录
    browser.find_element(By.CLASS_NAME, "login-btn").click()
    time.sleep(sleep_second)

def open_menu():
     # 查找菜单列表并点击进入
    browser.find_element(By.LINK_TEXT, "服务处办").click()
    time.sleep(sleep_second / 2)

def show_tasks():
    browser.find_element(By.LINK_TEXT, "任务处理").click()
    time.sleep(sleep_second / 2)
    browser.switch_to.frame("tab-content-01220045")
    browser.switch_to.frame("main-content")
    time.sleep(sleep_second/2)


def assigned_task():
    ac = browser.find_element(By.LINK_TEXT, "处理")
    ActionChains(browser).move_to_element(ac).click(ac).perform()
    time.sleep(sleep_second * 2)
    url = get_open_url("/cnsareacenterhandle?")
    open_window(url)
    browser.switch_to.window(browser.window_handles[1])
    dept_name = get_dept_name()
    if dept_name == None:
        close_window()
        browser.switch_to.window(browser.window_handles[0])
    else:
        browser.find_element(By.LINK_TEXT, "反馈").click()
        url = get_open_url("/areacenterfinishlayer?")
        open_window(url)
        print("处理意见")
        close_window()
        browser.switch_to.window(browser.window_handles[1])
        close_window()
        browser.switch_to.window(browser.window_handles[0])
    time.sleep(sleep_second/2)

if __name__ == "__main__":
    server = Server(proxy_path)
    server.start()
    proxy = server.create_proxy()

    browser = initBrowser()
    proxy.new_har("12345")
    browser.get(login_page)

    logon()
    open_menu()
    while True:
        show_tasks()
        assigned_task()

    server.stop()
