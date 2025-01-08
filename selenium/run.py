# encoding: utf-8

from selenium import webdriver  # 用于操作浏览器
from selenium.webdriver.chrome.options import Options  # 用于设置谷歌浏览器
from selenium.webdriver.chrome.service import Service  # 用于管理驱动
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browsermobproxy import Server
import time


class Automatic12345:

    def __init__(self) -> None:
        self.login_page = (
            "http://221.199.189.180:8090/cns-bmfw-web/bmfw/bmfwnewlogin/login"
        )
        self.proxy_path = (
            "/Users/jerry/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"
        )
        self.driver_path = "/Users/jerry/Downloads/chromedriver-mac-x64/chromedriver"
        # 设置浏览器、启动浏览器
        self.server = Server(self.proxy_path)
        self.server.start()
        self.proxy = self.server.create_proxy()
        self.proxy.new_har("12345")
        self.browser = self.init_browser()

    def init_browser(self):
        option = Options()
        option.add_argument("--no-sandbox")
        option.add_experimental_option("detach", True)
        option.add_argument("--proxy-server=%s" % self.proxy.proxy)
        browser = webdriver.Chrome(
            service=Service(self.driver_path),
            options=option,
        )
        browser.get(self.login_page)
        return browser

    def get_element(self, by, name):
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((by, name))
        )
        e = self.browser.find_element(by, name)
        return e

    def get_elements(self, by, name):
        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_all_elements_located((by, name))
        )
        e = self.browser.find_elements(by, name)
        return e

    def wait(self, func):
        WebDriverWait(self.browser, 20).until(func)

    def get_open_url(self, name):
        entries = self.proxy.har["log"]["entries"]

        for entry in reversed(entries):
            if "request" in entry.keys():
                if name in str(entry["request"]["url"]):
                    return str(entry["request"]["url"])

    def open_window(self, url):
        self.browser.execute_script('window.open("{url}")'.format(url=url))

    def close_window(
        self,
    ):
        self.browser.execute_script("window.close()")

    def get_dept_name(self):
        steps = self.get_elements(By.CLASS_NAME, "circulate-item")
        for step in steps:
            step_name, dept_name = "", ""
            try:
                step_name = self.get_element(
                    By.CLASS_NAME, "circulate-step2 "
                ).get_attribute("innerHTML")
            except:
                pass
            if step_name == "区办理单位":
                try:
                    dept_name = self.get_element(
                        By.CLASS_NAME, "circulate-step-label"
                    ).get_attribute("innerHTML")
                except:
                    pass
            if dept_name != "":
                start = dept_name.find("（")
                end = dept_name.find("）")
                return dept_name[start - 1 : end]

    def logon(self):
        # 输入用户名密码
        username = self.get_element(By.ID, "username")
        username.send_keys("15052600cbr01")
        psd = self.get_element(By.ID, "psd")
        psd.send_keys("Aa123-123")
        # 点击登录
        self.get_element(By.CLASS_NAME, "login-btn").click()

    def open_menu(self):
        # 查找菜单列表并点击进入
        self.get_element(By.LINK_TEXT, "服务处办").click()

    def show_tasks(self):
        self.get_element(By.LINK_TEXT, "任务处理").click()
        self.browser.switch_to.frame("tab-content-01220045")
        self.browser.switch_to.frame("main-content")

    def assigned_task(self, current_task):
        tasks = self.get_elements(By.LINK_TEXT, "处理")
        self.browser.execute_script("$(arguments[0]).click()", tasks[current_task])
        time.sleep(3)  # 等待任务层弹出
        url = self.get_open_url("/cnsareacenterhandle?")
        self.open_window(url)
        time.sleep(1)  # 等待新窗口弹出
        self.browser.switch_to.window(self.browser.window_handles[1])
        dept_name = self.get_dept_name()
        if dept_name == None:
            self.close_window()
            self.browser.switch_to.window(self.browser.window_handles[0])
        else:
            try:
                self.browser.find_element(By.LINK_TEXT, "反馈").click()
                url = self.get_open_url("/areacenterfinishlayer?")
                self.open_window(url)
                print("处理意见")
                # close_window()
                self.browser.switch_to.window(self.browser.window_handles[1])
                # close_window()
                self.browser.switch_to.window(self.browser.window_handles[0])
            except:
                pass

    def start(self):
        print("start...")
        self.logon()
        self.open_menu()
        current_task = 0
        self.show_tasks()
        self.assigned_task(current_task)
        # while True:
        #     try:
        #         show_tasks()
        #         assigned_task(current_task)
        #         current_task += 1
        #     except Exception as e:
        #         restart()

    def restart(self):
        print("restart...")
        self.browser.quit()
        self.browser = self.init_browser()
        self.start()


if __name__ == "__main__":
    try:
        ac = Automatic12345()
        ac.start()
    except Exception as e:
        print(e)
        ac.restart()
