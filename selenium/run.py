# encoding: utf-8

from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理驱动
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server
import time

login_page = "http://221.199.189.180:8090/cns-bmfw-web/bmfw/bmfwnewlogin/login"
proxy_path = "/Users/jerry/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"
driver_path = "/Users/jerry/Downloads/chromedriver-mac-x64/chromedriver"


# 设置浏览器、启动浏览器
server = Server(proxy_path)
server.start()
proxy = server.create_proxy()
proxy.new_har("12345")


def init_browser():
    option = Options()
    option.add_argument("--no-sandbox")
    option.add_experimental_option("detach", True)
    option.add_argument("--proxy-server=%s" % proxy.proxy)
    browser = webdriver.Chrome(
        service=Service(driver_path),
        options=option,
    )
    browser.get(login_page)
    return browser


browser = init_browser()


def get_element(by, name):
    WebDriverWait(browser, 20).until(EC.visibility_of_element_located((by, name)))
    e = browser.find_element(by, name)
    return e


def get_elements(by, name):
    WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located((by, name)))
    e = browser.find_elements(by, name)
    return e


def get_open_url(name):
    entries = proxy.har["log"]["entries"]

    for entry in reversed(entries):
        if "request" in entry.keys():
            if name in str(entry["request"]["url"]):
                return str(entry["request"]["url"])


def open_window(url):
    browser.execute_script('window.open("{url}")'.format(url=url))


def close_window():
    browser.execute_script("window.close()")


def get_dept_name():
    steps = get_elements(By.CLASS_NAME, "circulate-item")
    for step in steps:
        step_name, dept_name = "", ""
        try:
            step_name = get_element(By.CLASS_NAME, "circulate-step2 ").get_attribute(
                "innerHTML"
            )
        except:
            pass
        if step_name == "区办理单位":
            try:
                dept_name = get_element(
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
    username = get_element(By.ID, "username")
    username.send_keys("15052600cbr01")
    psd = get_element(By.ID, "psd")
    psd.send_keys("Aa123-123")
    # 点击登录
    get_element(By.CLASS_NAME, "login-btn").click()


def open_menu():
    # 查找菜单列表并点击进入
    get_element(By.LINK_TEXT, "服务处办").click()


def show_tasks():
    get_element(By.LINK_TEXT, "任务处理").click()
    browser.switch_to.frame("tab-content-01220045")
    browser.switch_to.frame("main-content")


def assigned_task(current_task):
    tasks = get_elements(By.LINK_TEXT, "处理")
    browser.execute_script("$(arguments[0]).click()", tasks[current_task])
    time.sleep(3)  # 等待任务层弹出
    url = get_open_url("/cnsareacenterhandle?")
    open_window(url)
    time.sleep(1)  # 等待新窗口弹出
    browser.switch_to.window(browser.window_handles[1])
    dept_name = get_dept_name()
    if dept_name == None:
        close_window()
        browser.switch_to.window(browser.window_handles[0])
    else:
        try:
            browser.find_element(By.LINK_TEXT, "反馈").click()
            url = get_open_url("/areacenterfinishlayer?")
            open_window(url)
            print("处理意见")
            # close_window()
            browser.switch_to.window(browser.window_handles[1])
            # close_window()
            browser.switch_to.window(browser.window_handles[0])
        except:
            pass


def start():
    print("start...")
    logon()
    open_menu()
    current_task = 0
    show_tasks()
    assigned_task(current_task)
    # while True:
    #     try:
    #         show_tasks()
    #         assigned_task(current_task)
    #         current_task += 1
    #     except Exception as e:
    #         restart()


def restart():
    print("restart...")
    global browser
    browser.quit()
    time.sleep(1)
    browser = init_browser()
    start()


if __name__ == "__main__":
    try:
        start()
    except Exception as e:
        print(e)
        restart()
